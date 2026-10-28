# Update an Article

**Framework**: AppleNewsAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update an existing article in your channel.

**Availability**:
- Apple News API 1.0+

## Mentions

- [Apple News API Release Notes](../AppleNews/apple-news-api-release-notes.md)

## Discussion

The Update an Article endpoint accepts a MIME multipart request, in multipart/form-data format, instead of JSON (application/json). In contrast to the [`Create an Article`](./post-channels-_channelid_-articles.md) request, all parts of an Update an Article request are optional except for the metadata section. The Update an Article request may also include the article’s Apple News Format document or any of the resources referenced in the document with a `bundle://` `URL`, each with its own MIME part.

For example, you can update a single image, the document text or layout, the metadata, or all of them at once. Other than the option to omit parts, the format of the Update an Article request is identical to the Create an Article request. Although you can omit MIME parts that you previously posted, you can’t partially update the Apple News Format document in the `article.json.` You can only replace it, not patch it.

If you remove a resource part in one update call and later decide you want to reference it in the article, you must upload the resource again (not just restore the reference).

Updating an article doesn’t change the timestamp of the article or its placement in your  feeds, such as the Today feed, channel feeds, and topic feeds.

Here are the guidelines for updating an existing article:

- For each update, provide the article ID and the `revision` token that matches the current revision of the article. This ensures that two users can’t update an article at the same time and lose data. If this happens, the client informs the second user (via the `WRONG_REVISION` error) that the specified revision was incorrect because the article was updated in the meantime. The second user must retrieve the new version before proceeding. The client can then attempt to merge the two versions and call Update an Article again, or can choose to overwrite the older version with the new version. To get the current revision, use the method call shown in [`Read Article Information`](./get-articles-_articleid_.md), or use a revision ID from an earlier Create an Article or Update an Article call.
- You must wrap all metadata fields in a data key. See “Example Code for Updating an Article with Metadata” below. The server returns the `INVALID_JSON` error if there is no data key in the request call.
- Include `isPreview` in the metadata to allow an update call to change the article’s preview/published state. Additionally, on update, you can make a preview article public (change `true` to `false`), but you can’t set a currently public article back to a preview state (change `false` to `true`).
- Use the `isHidden` property in the metadata  to hide and unhide an article in the Update an Article request.

### Example Code for Updating an Article Without Metadata

**Request**:

```
POST /articles/ArRPpLPE9QXu3sehS0rvxvA HTTP/1.1
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
    "revision": "AAAAAAAAAAAAAAAAAAAAev=="
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
--535e329ca936f79a19ac9a251f7d48f7--
```

**Response**:

```json
HTTP/1.1 200 OK
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
        "estimatedDelayInSeconds”: 126
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
"state": "PROCESSING_UPDATE",
"title": "Flother City Bears",
"maturityRating": null,
"warnings": [],
"isCandidateToBeFeatured": false,
"isSponsored": true,
"isPreview": true
}
}       
```

### Example Code for Updating an Article with Metadata

**Request**:

```
POST /articles/a91760f1-c169-47d2-9fc4-a7711341264d HTTP/1.1
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
    "targetTerritoryCountryCodes": ["GB", "US"],
    "links": {
      "sections": [
        "https://news-api.apple.com/sections/5cec0b36-529e-31bc-bc1e-3eaccbc15b97"
      ]
    },
    "revision": "AAAAAAAAAAAAAAAAAAAAeZ=="
  }
}
--535e329ca936f79a19ac9a251f7d48f7--
```

**Response**:

```json


HTTP/1.1 200 OK
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
        "https://news-api.apple.com/sections/5cec0b36-529e-31bc-bc1e-3eaccbc15b97"
      ]
    },
    "meta": {
      "throttling": {
        "isThrottled": true,
        "quotaAvailable": 0,
        "queueSize": 42,
        "estimatedDelayInSeconds": 1260
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
"revision": "AAAAAAAAAAAAAAAAAAAAfA==",
"state": "PROCESSING_UPDATE",
"title": "Flother City Lions",
"maturityRating": null,
"warnings": [],
"isCandidateToBeFeatured": false,
"isSponsored": true,
"isPreview": false,
"targetTerritoryCountryCodes": ["GB", "US"]
}
}
```

## Endpoint

`POST https://news-api.apple.com/articles/{articleId}`

## Parameters

### Path Parameters

- `articleId` (string) *(required)*: The UUID or the Share URL ID of the article you want to update.

## Request Body

**Content-Type**: `multipart/form-data`  
**Type**: `form-data`

The article’s Apple News Format JSON document and other assets, like PDFs, images, and fonts.

- `metadata` (Update Article Metadata Fields): Additional, non–Apple News Format data about the article. The revision token is a required field for each update article request.
- `Any Key` (binary): Assets such as images and fonts. Images can have `image/png`, `image/gif`, `image/jpeg`, or `application/octet-stream` as the content type. Fonts should have `application/octet-stream` as the content type.
- `article.json` (string) *(required)*: The Apple News Format document that contains this article’s content.

## Responses

- `200` OK (`ArticleResponse`, `application/json`):

  - The request was successful.
  - The server returns a warning for articles with a publication date before 2015.
- `202` Accepted (`ArticleResponse`, `application/json`): The Apple News team optimized the article, so your updates weren’t applied. Contact your Apple News technical representative if you need to make updates.
- `400` Bad Request (`Error`, `application/json`):

  - `ARTICLE_TERRITORY_NOT_ALLOWED`.  The channel doesn’t support the country code you provided, or the country code you provided is valid but isn’t an Apple News territory (US, UK, AU or CA). Key path: None.
  - `DOES_NOT_EXIST.` The section you specified doesn’t exist. Key path: `data.links.sections.#`.
  - `DUPLICATE_ARTICLE_FOUND`. An article with a source URL or a thumbnail is considered a duplicate if you post the article on the same channel, using the same title, source URL, or thumbnail, within a 24-hour period. An article without a source URL and thumbnail is considered a duplicate if you post the article on the same channel, using the same title, within a 24-hour period. The original article ID is provided in the `value` field.
  - `INCORRECT_ENCODING`. The body of the request isn’t encoded with the encoding specified in `Content-Encoding`. Key path: None.
  - `INCORRECT_HOST`. The section URL has the wrong hostname or port. Key path: `data.links.sections`.`#`.
  - `INVALID_ARTICLE_LANGUAGE`. The language of the article doesn’t match the language of the channel. Key path: None.
  - `INVALID_ARTICLE_TERRITORY`. A country code isn’t valid. Key path: None.
  - `INVALID_DOCUMENT`. The JSON in the Apple News Format document (`article.json`) is invalid. Test `article.json` with News Preview first. Key path: None.
  - `INVALID_MIME_MULTIPART`. The server can’t parse the request body as valid MIME-multipart. Key path: None.
  - `INVALID_PUBLISHING_DATE`. The publication date of the article can’t be before 1970. Key path: `metadata.datePublished`.
  - `INVALID_RESOURCE_TYPE`. The path in the section URL doesn’t start with /sections/. Key path: `data.links.sections.#`.
  - `INVALID_RESOURCE_ID`. The section URL has a section ID that is not a valid UUID. Key path: data.links.sections.#.
  - `INVALID_SCHEME`. The section `URL` must have the https scheme. Key path: `data`.`links.sections`.`#`.
  - `INVALID_TYPE`. The value you specified for the article is not of the correct type for that field. Key path: `channelId`.
  - `INVALID_URL` The section `URL` you specified is not a valid URL. Key path: `data.links.sections.#`.
  - `MIME_PART_MISSING_FILENAME.` The specified MIME part doesn’t have the filename parameter in its `Content-Disposition` header. Key path: {`mime_part_name`}.
  - `MIME_PART_TOO_SLOW`. The MIME part took too long to load from the request body. Key path: {`mime_part_name`}.
  - `MIME_PART_TOO_LARGE`. The MIME part is larger than the allowable size limit. Images exceeding 20 MB, fonts exceeding 5 MB, and attachments exceeding 50 MB generate this error. Key path: {`file name}`.
  - `MISSING`. The specified MIME part is required and was missing. Key path: {`mime_part_name}`.
  - `MISSING`. You didn’t supply the article `UUID` field in the request. Key path: *
  - `MISSING_RESOURCE_ID`. The section URL is missing the `section_id UUID`. Key path: `data`.`links`.`sections.#`.
  - `NOT_ALLOWED`. The section you specified doesn’t belong to the given channel. Key path: `data`.`links.sections`.`#`.
  - `ONLY_PREVIEW_ALLOWED`. This channel is currently allowed to publish preview articles only, but `isPreview` is `false`. Key path: None.
  - `PUBLISHING_NOT_ALLOWED`. This channel is currently not allowed to publish articles. Key path: None.
  - `REQUEST_BODY_TOO_LARGE`. The article bundle size is larger than the allowable size limit. An article bundle exceeding 450 MB generates this error. Key path: None.
  - `UNSUPPORTED_ENCODING`. The encoding specified in `Content-Type` or `Content-Transfer-Encoding` isn’t supported. Key path: None.
  - `WRONG_REVISION.` The revision specified doesn’t match the current revision, most likely because another call updated the article. Key path: `data.revision`.
- `401` Unauthorized (`Error`, `application/json`): You didn’t include the `Authorization` header. Key path: None.
- `403` Forbidden (`Error`, `application/json`): You tried to access a channel your API key doesn’t have permission to access. Key path: None.
- `404` Not Found (`Error`, `application/json`):

  - The endpoint you tried to access doesn’t exist. Key path: None.
  - The article you tried to access doesn’t exist. Key path: `articleId`.
- `409` Conflict (`Error`, `application/json`): The revision specified doesn’t match the current revision, most likely because another call updated the article. Key path: `data.revision`.
- `429` Too Many Requests (`Error`, `application/json`): You exceeded the number of articles that you can update within the specific time window. The response header `<Retry-After: delay-seconds>` indicates the time in seconds you need to wait before sending a new update request.

## See Also

### Articles
- [Create an Article](./post-channels-_channelid_-articles.md)
  Publish an article to your channel.
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
- [Search Articles in a Channel](./get-channels-_channelid_-articles.md)
  See a list of all articles in a channel that match the specified search criteria.
- [Search Articles in a Section](./get-sections-_sectionid_-articles.md)
  See a list of all articles in a section that match the specified search criteria.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/post-articles-_articleid_)*