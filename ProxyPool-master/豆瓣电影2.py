# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:30:51 2018

@author: asus
"""
from bs4 import BeautifulSoup
import re
import basicSpider
crawl_queue = []  #待爬队列
crawled_queue = [] #已爬队列

def save_file(movieInfo):
    """
    写文件的操作,这里使用的追加的方式来写文件
    """
    with open("doubanMovie.txt","ab") as f:
        #lock.acquire()
        f.write(movieInfo.encode("utf-8"))
        #lock.release()

def CrawlMovieInfo(url):
    """
    抓取一页数据的逻辑
    """
    global crawl_queue
    global crawled_queue
    
    html = get_html(url)
    pattern = re.compile('(https://[\s\S]*?3516235/\?start=.*)')
    itemUrls = re.findall(pattern, html)
    print(itemUrls)
    
if __name__ == '__main__':
    CrawlMovieInfo('https://www.douban.com/doulist/3516235/?start=25&sort=seq&playable=0&sub_type=')