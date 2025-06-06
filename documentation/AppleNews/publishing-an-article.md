# Publishing an Article

**Framework**: Apple News

Build a URL and article body for the publish-article request.

#### Overview

To publish an article to your channel, you make a multipart POST request consisting of at least one MIME part named `article.json`. You provide additional parts for each resource that uses a URL in the format `bundle:// URL`. See [`Create an Article`](https://developer.apple.com/documentation/applenewsapi/post-channels-_channelid_-articles).

- Build a publish-article URL.
- Build the article body.
- (Optional) Include a `metadata.json` file.
- Send the publish-article request.

##### Copy This Code

Open any text editor to copy this code. Save the file as `create_article.py`.

```python
import sys
import requests
import base64
import hmac
import random
import os
import glob
import hashlib
from datetime import datetime

class PublisherAPI:
    channel_id = ""
    current_action = ""
    key_id = ""
    key_secret = ""
    article_directory = ""
    url = ""

    def send_request(self, method, url, body=None, content_type=None):
        date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        if body:
            url = self.url + url
        canonical_request = method + url + date
        canonical_request = canonical_request.encode()

        if body:
            canonical_request += content_type + body

        signature = self.create_signature(canonical_request)
        authorization = "HHMAC; key=%s; signature=%s; date=%s" % (
            self.key_id, signature, date)
        headers = {"Authorization": authorization}
        if body:
            headers["Content-Type"] = content_type

        return requests.request(method, url, headers=headers, data=body)

    def create_signature(self, canonical_request):
        key_bytes = base64.b64decode(self.key_secret)
        
        message = canonical_request
        secret = self.key_secret.encode("utf-8")

        signature = base64.b64encode(
          hmac.new(key_bytes, message,
              digestmod=hashlib.sh 256).digest()).decode("utf-8")
        return signature

    def create_article(self):
        method = "POST"
        path = "%s/articles" % self.channel_id
        body, content_type = self.build_article_body()
        return self.send_request(method, path, body, content_type)

    def build_article_body(self):
        boundary = str(random.getrandbits(64))
        boundary = boundary.encode()
        content_type = b"multipart/form-data; boundary=%s" % boundary
        filenames = glob.glob('%s/*' % self.article_directory)
        parts = filter(None, map(lambda f: self.build_mime_part(boundary, f), filenames))
        if not parts:
            sys.exit("%s doesn't appear to be a valid article bundle!" %  self.article_directory)
        body = b"\r\n".join(parts)
        body += b"\r\n--%s--" % boundary

        return body, content_type

    def build_mime_part(self, boundary, filename):
        basename = os.path.basename(filename)
        content_type = self.guess_content_type(basename)
        if content_type == None:
            return None
        content_type = content_type.encode()
        part = bytearray()
        part = b"--%s\r\n" % boundary
        part += b"Content-Type: %s\r\n" % content_type
        if basename == 'metadata.json':
           part += b"Content-Disposition: form-data; name=metadata; size=%d\r\n\r\n" % os.stat(filename).st_size
        else:
            basename = basename.encode()
            part += b"Content-Disposition: form-data; filename=%s; size=%d\r\n\r\n" % (basename, os.stat(filename).st_size)
        with open(filename,'rb') as f:
            part += f.read()
        return part

    def guess_content_type(self, filename):
        extension = os.path.splitext(filename)[1]
        if filename == "article.json" or filename == "metadata.json":
            return "application/json"
        elif extension == ".jpg" or extension == ".jpeg":
            return "image/jpeg"
        elif extension == ".gif":
            return "image/gif"
        elif extension == ".png":
            return "image/png"
        return None

    def read_channel(self):
        method = "GET"
        url = self.url + "%s" % self.channel_id
        return self.send_request(method, url)

    def main(self):
        if self.current_action == "readChannel":
            response = self.read_channel()
        elif self.current_action == "createArticle":
            response = self.create_article()
        else:
            response = {
                "status_code": 400,
                "response": "{\"errors\":[{\"code\":\"UNKNOWN_COMMAND\"}]}"
            }
        return response


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print ('no arguments')
        exit()
    
    publisherAPI = PublisherAPI()
    publisherAPI.url = sys.argv[1] + "/channels/"
    publisherAPI.channel_id = sys.argv[2]
    publisherAPI.key_id = sys.argv[3]
    publisherAPI.key_secret = sys.argv[4]

    if len(sys.argv) == 6:
        publisherAPI.article_directory = sys.argv[5]
        publisherAPI.current_action = "createArticle"
    else:
        publisherAPI.current_action = "readChannel"
    
    response = publisherAPI.main()

    print(response.status_code)
    print(response.text)
```

##### Create the Metadata File

This step is optional. You might want to include a metadata file to provide additional data about the article.

To create the metadata file, open any text editor and include optional metadata fields. Save the file as `metadata.json`. For information about supported metadata fields, see [`Create Article Metadata Fields`](https://developer.apple.com/documentation/applenewsapi/create-article-metadata-fields).

This is an example `metadata.json` file.

```json
{
   "data": {
   "isPreview": true,
   "isHidden": true
   "maturityRating": null,
   "links": {
       "sections": [
         "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180",
         "https://news-api.apple.com/sections/5cec0b36-529e-31bc-bc1e-3eaccbc15b97"
       ]
   }
}
```

##### Run the Script

Start the command prompt and change to the directory containing `create_article.py`. Run this script to make a [`Create an Article`](https://developer.apple.com/documentation/applenewsapi/post-channels-_channelid_-articles) request to the Apple News API. This script takes five arguments: API URL (https://news-api.apple.com), Channel ID, Key ID, Secret, and the path to the article directory.

```python
python create_article.py https://news-api.apple.com channel_id key_id key_secret path/to/article/directory/
```

##### Result

The server returns the `ArticleResponse` object. For more information, see [`Article`](https://developer.apple.com/documentation/applenewsapi/article), `ArticleLinks`, and [`Meta`](https://developer.apple.com/documentation/applenewsapi/meta).

##### How It Works

To publish an article, you build the publish-article URL using the POST method.

```python
method = "POST"
path = "%s/articles" % self.channel_id
```

Next, you build the request body and set the content type. The body contains one or more parts based on the number of files in your article and the content type, as shown here:

```python
body, content_type = self.build_article_body()
```

Next, you create a boundary to separate the request parts, as shown here. This is a unique string.

```python
boundary = str(random.getrandbits(64))
```

Next, you declare the content type along with the boundary, as shown here:

```python
content_type = b"multipart/form-data; boundary=%s" % boundary
```

The content type looks like this:

```python
multipart/form-data; boundary=14970318244633716999
```

Next, you build the MIME parts for each file in the article you want to publish.

```python
filenames = glob.glob('%s/*' % self.article_directory)
parts = filter(None, map(lambda f: self.build_mime_part(boundary, f), filenames))
```

When you build the MIME parts, only use the Apple News-supported file-format extensions; for example, JSON, JPEG, GIF, and PNG. See [`Preparing Image, Video, Audio, Music, and ARKit Assets`](preparing-image-video-audio-music-and-arkit-assets.md).

```python
extension = os.path.splitext(filename)[1]
if filename == "article.json" or filename == "metadata.json":
    return "application/json"
elif extension == ".jpg" or extension == ".jpeg":
    return "image/jpeg"
elif extension == ".gif":
    return "image/gif"
elif extension == ".png":
    return "image/png"
return None
```

Once you determine the file type, you construct each part from `Content-Type`, `Content-Disposition`, and the file data, as shown here. If you include the `metadata.json` file, the `Content-Disposition` header adds `name=metadata` to ensure that the system recognizes the metadata for the article.

```python
part = b"--%s\r\n" % boundary
part += b"Content-Type: %s\r\n" % content_type
  if basename == 'metadata.json':
    part += b"Content-Disposition: form-data; name=metadata; size=%d\r\n\r\n" % os.stat(
                filename).st_size
    else:
      basename = basename.encode()
      part += b"Content-Disposition: form-data; filename=%s; size=%d\r\n\r\n" % (
                basename, os.stat(filename).st_size)
    with open(filename, 'rb') as f:
      part += f.read()
```

A part looks like this:

```other
--6030599197195158890
Content-Type: image/jpeg
Content-Disposition: form-data; filename=photo.jpg; size=20483
{binary data}
```

Next, you join the parts together and denote the end of the multipart form data by the boundary, preceded by two dashes (`--`).

```python
body = b"\r\n".join(parts)
body += b"\r\n--%s--" % boundary
```

Finally, you combine the canonical request with the request body and make the request.

```python
def send_request(self, method, url, body=None, content_type=None):
    date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    if body:
        url = self.url + url
    canonical_request = method + url + date
    canonical_request = canonical_request.encode()
    if body:
        canonical_request += content_type + body

    signature = self.create_signature(canonical_request)
    authorization = "HHMAC; key=%s; signature=%s; date=%s" % (self.key_id, signature, date)
    headers = {"Authorization": authorization}
    if body:
        headers["Content-Type"] = content_type

    return requests.request(method, url, headers=headers, data=body)
```

## See Also

- [Making an HTTP Request to the Apple News API](making-an-http-request-to-the-apple-news-api.md)
  Create the URL, set the method, and send the request.
- [Signing the HTTP Request](signing-the-http-request.md)
  Sign the canonical request and send the custom authorization header to the Apple News API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/publishing-an-article)*