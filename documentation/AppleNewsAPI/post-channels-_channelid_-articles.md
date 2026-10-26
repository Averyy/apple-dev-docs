# Create an Article

**Framework**: AppleNewsAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Publish an article to your channel.

**Availability**:
- Apple News API 1.0+

## Mentions

- [Apple News API Release Notes](../AppleNews/apple-news-api-release-notes.md)
- [Publishing an Article](../AppleNews/publishing-an-article.md)
- [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md)
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)

#### Discussion

Use the Create an Article endpoint to publish an article to your channel.

Here are the guidelines for Apple News Format documents and resources:

- A Create an Article request must consist of at least one `MIME` part that contains the article’s Apple News Format document. This part must have filename set to `article.json`. See “Example Code for Creating an Article Without Metadata” below.
- The server requires additional parts for each resource referenced in the Apple News Format document that uses a `URL` in this format: `bundle:// URL`.
- Each part must have a `Content-Disposition` header. The disposition must be form-data, and you must specify the filename parameter of `Content-Disposition`.
- In resource parts, the filename parameter must match the path of the `bundle://` `URL` in the Apple News Format document that references this file. For example, if the document references a URL of `bundle://logo.png`, there must be a `MIME` part with filename set to `logo.png`. For resource parts, the valid values for `Content-Type` are `image/jpeg`, `image/png`, `image/gif`, and `application/octet-stream`.
- When using a remote image, the URL must be in `http://` or `https://` format. No additional parts are required in the URL for remote images.

See [Apple News API Tutorial](../AppleNews/apple-news-api-tutorial.md) to learn how to publish an article using the Apple News API.

Here are the guidelines for Apple News Format metadata:

- You can include an optional metadata part to provide additional non–Apple News Format data about the article, such as `isSponsored` and `maturityRating`. See [`Create Article Metadata Fields`](./create-article-metadata-fields.md). The metadata part can also specify any sections for the article by URL.
- You must wrap all metadata fields in a data key. See “Example Code for Creating an Article with Metadata” below_._ The `INVALID_JSON` error is thrown if there is no `data` key in the request call.

Here are the guidelines for Apple News Format sections:

- To publish the article to the channel’s default section, omit `links.sections`.
- To get information about a specific section, such as the section ID, use the [`Read Section Information`](./get-sections-_sectionid_.md) endpoint.
- To publish a standalone article outside of sections, set `sections` to `[]` (an empty array). Standalone articles don’t appear in your channel, but still appear in topics and search results, and may appear in For You.

Here are general guidelines for Apple News Format:

- For articles with a source URL or thumbnail, avoid posting more than one article on the same channel using the same title, source URL, or thumbnail, within a 24-hour period. An article is considered a duplicate if these conditions are met.
- For articles without a source URL and thumbnail, avoid posting more than one article on same channel, using the same title, within a 24-hour period. An article is considered a duplicate if these conditions are met.
- When you create an article, be sure to retain the article ID or the self URL that’s returned in the response. You need the article ID to read, update, and delete an article.
- To publish older articles, use the metadata properties in Apple News Format. If you set an older publication date, the article appears earlier in the feed. See [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) in Apple News Format documentation. Articles are sorted by publication date.
- A canonical URL is required to do data collection and reporting for comScore analytics.
- Don’t change the canonical URL of the article after it has been set.

##### Example Code for Creating an Article Without Metadata

**Request**:

```
POST /channels/63a75491-2c4d-3530-af91-819be8c3ace0/articles HTTP/1.1
Host: news-api.apple.com
Accept: application/json
Content-Type: multipart/form-data; boundary=535e329ca936f79a19ac9a251f7d48f7
Content-Length: 94348
Authorization: HHMAC; key="1e3gfc5e-e9f8-4232-a6be-17bf40edad09"; signature="gJYsk8qm+6wpONE8twX/yDlGRt0UzS7Qn32yHNpiwnM="; date="2015-03-05T03:00:27Z"
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: application/json
Content-Disposition: form-data; filename=article.json; name=article.json
{
    "version": "1.7",
    "identifier": "SampleArticle",
    "language": "en",
    "title": "Apple News App",
    "subtitle": "A look at the features of the News iOS app",
    "layout": {
        "columns": 7,
        "width": 1024,
        "margin": 75,
        "gutter": 20
    },
    "components": [
        {
            "role": "title",
            "text": "Apple News App",
            "textStyle": "title"
        },
        {
            "role": "body",
            "text": "The Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
        },
        {
            "role": "photo",
            "URL": "bundle://image.jpg"
        }
    ],
    "documentStyle": {
        "backgroundColor": "#F7F7F7"
    },
    "componentTextStyles": {
        "default": {
            "fontName": "Helvetica",
            "fontSize": 13,
            "linkStyle": {
                "textColor": "#428bca"
            }
        },
        "title": {
            "fontName": "Helvetica-Bold",
            "fontSize": 30,
            "hyphenation": false
        },
        "default-body": {
        "fontName": "Helvetica",
        "fontSize": 13
        }
    }
}
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: image/jpeg
Content-Disposition: form-data; filename=mountain-lions.jpg; name=my_image
{binary content of mountain-lions.jpg}
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: application/octet-stream
Content-Disposition: form-data; filename=gradient.png; name=a_gradient
{binary content of gradient.png}
--535e329ca936f79a19ac9a251f7d48f7--
```

**Response**:

```json
HTTP/1.1 201 OK
Date: Thu, 05 Mar 2015 02:53:54 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
{
  "data": {
    "createdAt": "2015-03-05T02:57:59Z",
    "modifiedAt": "2015-03-05T02:57:59Z",
    "id": "a91760f1-c169-47d2-9fc4-a7711341264d",
    "type": "article",
    "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvA",
    "links": {
      "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
      "self": "https://news-api.apple.com/articles/a91760f1-c169-47d2-9fc4-a7711341264d",
      "sections": [
        "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180"
      ]
    },
    "meta": {
      "throttling": {
        "isThrottled": true,
        "quotaAvailable": 0,
        "queueSize": 42,
        "estimatedDelayInSeconds”: 1260  
    }
    },
"document": {
  "version": "1.7",
  "identifier": "SampleArticle",
  "language": "en",
  "title": "Apple News App",
  "subtitle": "A look at the features of the News iOS app",
  "layout": {
    "columns": 7,
    "width": 1024,
    "margin": 75,
    "gutter": 20
  },
  "components": [
    {
      "role": "title",
      "text": "Apple News App",
      "textStyle": "title"
    },
    {
      "role": "body",
      "text": "The Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    },
    {
      "role": "photo",
      "URL": "bundle://image.jpg"
    }
  ],
  "documentStyle": {
    "backgroundColor": "#F7F7F7"
  },
  "componentTextStyles": {
    "default": {
      "fontName": "Helvetica",
      "fontSize": 13,
      "linkStyle": {
        "textColor": "#428bca"
      }
    },
    "title": {
      "fontName": "Helvetica-Bold",
      "fontSize": 30,
      "hyphenation": false
    },
    "default-body": {
      "fontName": "Helvetica",
      "fontSize": 13
    }
  }
},
"revision": "AAAAAAAAAAAAAAAAAAAAew==",
"state": "PROCESSING",
"title": "Flother City Lions",
"maturityRating": null,
"warnings": [],
"isCandidateToBeFeatured": false,
"isSponsored": false,
"isPreview": false
}
}
```

##### Example Code for Creating an Article with Metadata

**Request**:

```


POST /channels/63a75491-2c4d-3530-af91-819be8c3ace0/articles HTTP/1.1
Host: news-api.apple.com
Accept: application/json
Content-Type: multipart/form-data; boundary=535e329ca936f79a19ac9a251f7d48f7
Content-Length: 94348
Authorization: HHMAC; key="1e3gfc5e-e9f8-4232-a6be-17bf40edad09"; signature="gJYsk8qm+6wpONE8twX/yDlGRt0UzS7Qn32yHNpiwnM="; date="2015-03-05T03:00:27Z"
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: application/json
Content-Disposition: form-data; name=metadata
{
    "data": {
        "isCandidateToBeFeatured": "false",
        "isSponsored": true,
        "isPreview": true,
        "maturityRating": null,
        "targetTerritoryCountryCodes": ["GB", "US"],
        "links": {
            "sections": [
                "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180",
                "https://news-api.apple.com/sections/5cec0b36-529e-31bc-bc1e-3eaccbc15b97"
            ]
        }
    }
}
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: application/json
Content-Disposition: form-data; filename=article.json; name=article.json
{
    "version": "1.7",
    "identifier": "SampleArticle",
    "language": "en",
    "title": "Apple News App",
    "subtitle": "A look at the features of the News iOS app",
    "layout": {
        "columns": 7,
        "width": 1024,
        "margin": 75,
        "gutter": 20
    },
    "components": [
        {
            "role": "title",
            "text": "Apple News App",
            "textStyle": "title"
        },
        {
            "role": "body",
            "text": "The Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
        },
        {
            "role": "photo",
            "URL": "bundle://image.jpg"
        }
    ],
    "documentStyle": {
        "backgroundColor": "#F7F7F7"
    },
    "componentTextStyles": {
        "default": {
            "fontName": "Helvetica",
            "fontSize": 13,
            "linkStyle": {
                "textColor": "#428bca"
            }
        },
        "title": {
            "fontName": "Helvetica-Bold",
            "fontSize": 30,
            "hyphenation": false
        },
        "default-body": {
        "fontName": "Helvetica",
        "fontSize": 13
        }
    }
}
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: image/jpeg
Content-Disposition: form-data; filename=mountain-lions.jpg; name=my_image
{binary content of mountain-lions.jpg}
--535e329ca936f79a19ac9a251f7d48f7
Content-Type: application/octet-stream
Content-Disposition: form-data; filename=gradient.png; name=a_gradient
{binary content of gradient.png}
-535e329ca936f79a19ac9a251f7d48f7--
```

**Response**:

```json


HTTP/1.1 201 OK
Date: Thu, 05 Mar 2015 02:53:54 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
{
  "data": {
    "createdAt": "2015-03-05T02:57:59Z",
    "modifiedAt": "2015-03-05T02:57:59Z",
    "id": "a91760f1-c169-47d2-9fc4-a7711341264d",
    "type": "article",
    "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvA",
    "links": {
      "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
      "self": "https://news-api.apple.com/articles/a91760f1-c169-47d2-9fc4-a7711341264d",
      "sections": [
        "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180",
        "https://news-api.apple.com/sections/5cec0b36-529e-31bc-bc1e-3eaccbc15b97"
      ]
    },
    "meta": {
      "throttling": {
        "isThrottled": true,
        "quotaAvailable": 0,
        "queueSize": 42,
        "estimatedDelayInSeconds”: 1260  
      }
    },
"document": {
  "version": "1.7",
  "identifier": "SampleArticle",
  "language": "en",
  "title": "Apple News App",
  "subtitle": "A look at the features of the News iOS app",
  "layout": {
    "columns": 7,
    "width": 1024,
    "margin": 75,
    "gutter": 20
  },
  "components": [
    {
      "role": "title",
      "text": "Apple News App",
      "textStyle": "title"
    },
    {
      "role": "body",
      "text": "The Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    },
    {
      "role": "photo",
      "URL": "bundle://image.jpg"
    }
  ],
  "documentStyle": {
    "backgroundColor": "#F7F7F7"
  },
  "componentTextStyles": {
    "default": {
      "fontName": "Helvetica",
      "fontSize": 13,
      "linkStyle": {
        "textColor": "#428bca"
      }
    },
    "title": {
      "fontName": "Helvetica-Bold",
      "fontSize": 30,
      "hyphenation": false
    },
    "default-body": {
      "fontName": "Helvetica",
      "fontSize": 13
    }
  }
},
"revision": "AAAAAAAAAAAAAAAAAAAAew==",
"state": "PROCESSING",
"title": "Flother City Lions",
"maturityRating": null,
"warnings": [
  
],
"isCandidateToBeFeatured": false,
"isSponsored": true,
"isPreview": true,
"targetTerritoryCountryCodes": ["GB", "US"]
}
}
```

## Endpoint

`POST https://news-api.apple.com/channels/{channelId}/articles`

## Parameters

### Path Parameters

- `channelId` (string) *(required)*: The UUID of the channel to publish the article to.

## Request Body

**Content-Type**: `multipart/form-data`  
**Type**: `form-data`

The article’s Apple News Format JSON document and other assets, like PDFs, images, and fonts.

- `metadata` (Create Article Metadata Fields): You can include an optional metadata to provide additional non–Apple News Format data about the article. The metadata part can also specify any sections for the article, by URL.
- `Any Key` (binary): Assets such as images and fonts. Images can have `image/png`, `image/gif`, `image/jpeg`, or `application/octet-stream` as the content type. Fonts should have `application/octet-stream` as the content type.
- `article.json` (string): The Apple News Format document that contains this article’s content.

## Responses

- `201` Created (`ArticleResponse`, `application/json`):

  - You successfully created the article.
  - The server returns a warning for articles with a publication date before 2015.
- `400` Bad Request (`Error`, `application/json`):

  - `ARTICLE_TERRITORY_NOT_ALLOWED.` The channel doesn’t support the country code you provided, or the country code you provided is valid but isn’t an Apple News territory (US, UK, AU or CA). Key path: None.
  - `DOES_NOT_EXIST`. The section you specified doesn’t exist. Key path: `data.links.sections.#`.
  - `DUPLICATE_ARTICLE_FOUND`. An article with a source URL or a thumbnail is considered a duplicate if you post the article on the same channel, using the same title, source URL, or thumbnail, within a 24-hour period. An article without a source URL and thumbnail is considered a duplicate if you post the article on the same channel, using the same title, within a 24-hour period. The server provides the original article ID in the response.
  - `INCORRECT_ENCODING`. The body of the request isn’t encoded with the encoding specified in `Content-Encoding`. Key path: None.
  - `INCORRECT_HOST`. The section URL has the wrong hostname or port. Key path: data.links.sections.#.
  - `INVALID_ARTICLE_LANGUAGE`. The language of the article doesn’t match the language of the channel. Key path: None.
  - `INVALID_ARTICLE_TERRITORY`. A country code isn’t valid. Key path: None.
  - `INVALID_DOCUMENT`. The JSON in the Apple News Format document (`article.json`) is invalid. Test the `article.json` file with News Preview first. Key path: None.
  - `INVALID_MIME_MULTIPART`. The server can’t parse the request body as valid `MIME-multipart`. Key path: None.
  - `INVALID_PUBLISHING_DATE`. The publication date of the article can’t be before 1970. Key path: `metadata.datePublished`.
  - `INVALID_RESOURCE_ID`. The section URL has a section ID that isn’t a valid UUID. Key path: `data.links.sections.#`.
  - `INVALID_RESOURCE_TYPE`. The path in the section URL doesn’t start with `/sections/`. Key path: `data.links.sections.#`.
  - `INVALID_SCHEME`. The section URL must have the https scheme. Key path: `data.links.sections.#`.
  - `INVALID_TYPE`. The value you specified for the article is not of the correct type for that field. Key path: `channelId`.
  - `INVALID_URL` The section URL you specified isn’t a valid URL. Key path: `data.links.sections.#`.
  - `MIME_PART_MISSING_FILENAME`. The specified `MIME` part doesn’t have the filename parameter in its `Content-Disposition` header. Key path: `{mime_part_name}`.
  - `MIME_PART_TOO_SLOW`. The MIME part took too long to load from the request body. Key path: {`mime_part_name`}.
  - `MIME_PART_TOO_LARGE`.  The MIME part is larger than the allowable size limit. Images exceeding 20 MB, fonts exceeding 5 MB, and attachments exceeding 50 MB generate this error. Key path: {`file name}`.
  - `MISSING`. The specified `MIME` part is required and was missing. Key path: `{mime_part_name}`.
  - `MISSING`. You didn’t include the Article UUID or the Share URL ID field in the request. Key path: *
  - `MISSING_RESOURCE_ID`. The section URL is missing the `section_id` UUID. Key path: `data.links.sections.#`.
  - `NOT_ALLOWED`. The section you specified doesn’t belong to the given channel. Key path: `data.links.sections.#`.
  - `ONLY_PREVIEW_ALLOWED`. This channel is currently allowed to publish preview articles only, but `isPreview` is false. Key path: None.
  - `PUBLISHING_NOT_ALLOWED`. This channel is currently not allowed to publish articles. Key path: None.
  - `REQUEST_BODY_TOO_LARGE`. The article bundle size is larger than the allowable size limit. An article bundle exceeding 450 MB generates this error. Key path: None.
  - `UNSUPPORTED_ENCODING`. The encoding specified in `Content-Type` or `Content-Transfer-Encoding` isn’t supported. Key path: None.
- `401` Unauthorized (`Error`, `application/json`): You didn’t include the `Authorization` header. Key path: None.
- `403` Forbidden (`Error`, `application/json`): You tried to access a channel your API key doesn’t have permission to access. Key path: None.
- `404` Not Found (`Error`, `application/json`):

  - The endpoint you tried to access doesn’t exist. Key path: None.
  - The channel you want to add an article to doesn’t exist. Key path: `channelId`.
- `429` Too Many Requests (`Error`, `application/json`): You exceeded the number of articles that can be published within the allowed time window. The response header `<Retry-After: delay-seconds>` indicates the time in seconds you need to wait before sending a new request to publish articles.

## See Also

### Articles
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
- [Search Articles in a Channel](./get-channels-_channelid_-articles.md)
  See a list of all articles in a channel that match the specified search criteria.
- [Search Articles in a Section](./get-sections-_sectionid_-articles.md)
  See a list of all articles in a section that match the specified search criteria.
- [Update an Article](./post-articles-_articleid_.md)
  Update an existing article in your channel.
- [Delete an Article](./delete-articles-_articleid_.md)
  Delete the specified article from your channel.
- [object Create Article Metadata Fields](./create-article-metadata-fields.md)
  See the optional metadata fields for the Create an Article Request.
- [object ArticleLinksRequest](./articlelinksrequest.md)
  See the required field for the Create an Article request.
- [object Update Article Metadata Fields](./update-article-metadata-fields.md)
  See the metadata fields for the Update an Article request.
- [object Article](./article.md)
  See the fields the article endpoints returned.
- [object ArticleResponse](./articleresponse.md)
  See which objects make up the Create an Article, Read an Article, and Update an Article responses.
- [object ArticleLinksResponse](./articlelinksresponse.md)
  See the links the article endpoints returned.
- [object SearchResponse](./searchresponse.md)
  See the fields the search article endpoints returned.
- [object Meta](./meta.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Read an Article endpoints.
- [object Throttling](./throttling.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Update an Article endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/post-channels-_channelid_-articles)*