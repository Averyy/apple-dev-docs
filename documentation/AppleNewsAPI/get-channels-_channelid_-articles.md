# Search Articles in a Channel

**Framework**: AppleNewsAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

See a list of all articles in a channel that match the specified search criteria.

**Availability**:
- Apple News API 1.0+

## Discussion

A Search Articles request returns a list of all articles in a channel that were created between `fromDate` and `toDate`. The results of this call are paginated, with a maximum page size of 100. Each response contains a link to the next page of results.

### Example

**Request**:

```
GET /channels/63a75491-2c4d-3530-af91-819be8c3ace0/articles?pageSize=2 HTTP/1.1
Host: news-api.apple.com
Accept: application/json
Authorization: HHMAC; key="1e3gfc5e-e9f8-4232-a6be-17bf40edad09"; signature="irqw07DCRQLtx/40Z2VhNc7sl3nB1PKII374R7AHjUQ="; date="2015-02-28T00:03:31Z"
```

**Response**:

```json
HTTP/1.1 200 OK
Date: Sat, 28 Feb 2015 00:51:41 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
{
  "data": [
    {
      "createdAt": "2015-02-28T00:49:36Z",
      "modifiedAt": "2015-02-28T00:49:36Z",
      "id": "a3caeb08-b9db-4002-b379-cde305d74be7",
      "type": "article",
      "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvA",
      "links": {
        "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
        "self": "https://news-api.apple.com/articles/a3caeb08-b9db-4002-b379-cde305d74be7",
        "sections": [
          "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180",
          "https://news-api.apple.com/sections/0a664711-242f-6b13-1fa1-a6f081549989"
        ]
      },
      "revision": "AAAAAAAAAAAAAAAAAAAAew==",
      "state": "LIVE",
      "title": "Tie Goes to the Runner",
      "maturityRating": null,
      "warnings": [
        
      ],
      "isCandidateToBeFeatured": false,
      "isSponsored": false,
      "isPreview": false
    },
    {
      "createdAt": "2015-02-28T02:55:35Z",
      "modifiedAt": "2015-02-28T02:55:42Z",
      "id": "a800da5a-dcce-4e9b-85ec-88b269632586",
      "type": "article",
      "shareUrl": "https://apple.news/AARC-lzLXNHqWvwN0UN_C1Q",
      "links": {
        "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
        "self": "https://news-api.apple.com/articles/a800da5a-dcce-4e9b-85ec-88b269632586",
        "sections": [
          "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180"
        ]
      },
      "revision": "AAAAAAAAAAAAAAAAAAAAAB==",
      "state": "LIVE",
      "title": "NL East Roundup",
      "maturityRating": null,
      "warnings": [],
      "isCandidateToBeFeatured": false,
      "isSponsored": false,
      "isPreview": false
    }
  ],
  "links": {
    "next": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0/articles? pageSize=2&amp;pageToken=AoE/BTAwMzNiZTIxLTBkY2EtNGJiMi05YTQ0LTZhNWMzZjgzNzcxMw==",
    "self": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0/articles?pageSize=2"
  },
  "meta": {
    "nextPageToken": "AoE/BTAwMzNiZTIxLTBkY2EtNGJiMi05YTQ0LTZhNWMzZjgzNzcxMw=="
  }
}
```

## Endpoint

`GET https://news-api.apple.com/channels/{channelId}/articles`

## Parameters

### Path Parameters

- `channelId` (string) *(required)*: The UUID of the channel to search.

### Query Parameters

- `fromDate` (string): If specified, the server only returns articles with a `createdAt` date later than `fromDate`.
- `pageSize` (integer): The number of articles to return on each page. This value must be an integer between 1 and 100 (inclusive).

  **Default**: `10`
- `pageToken` (string): An opaque token that specifies the page to view. The server returns links with the URL in each response. It also includes the `pageToken` for the next page.
- `sortDir` (string): Indicates whether to return oldest articles first (`ASC`) or newest articles first (`DESC`).

  **Default**: `DESC`
- `toDate` (string): If specified, the server only returns articles with a `createdAt` date earlier than `toDate`.

## Responses

- `200` OK (`SearchResponse`, `application/json`): The request was successful.
- `400` Bad Request (`Error`, `application/json`):

  - `INVALID`. The `pageToken` parameter isn’t a valid token returned in a `next` link or `nextPageToken` field. Key path: `pageToken`
  - `INVALID.` The `sortDir` parameter is not ASC or `DESC`. Key path: `sortDir`
  - `INVALID.` The `fromDate` parameter isn’t in ISO 8601 date format. Key path: `fromDate`
  - `INVALID.`The `toDate` parameter isn’t in ISO 8601 date format. Key path: `toDate`
  - `INVALID.` The `pageSize` parameter isn’t an integer in the range 1 to 100, inclusive. Key path: `pageSize`
  - `INVALID_TYPE`. The value specified for `channelId` is not of the correct type for that field. Key path: `channelId`
  - `MISSING`. You didn’t include the Channel UUID field in the request. Key path: `*`
- `401` Unauthorized (`Error`, `application/json`): You didn’t include the `Authorization` header. Key path: N/A
- `403` Forbidden (`Error`, `application/json`): You tried to access a channel your API key doesn’t have permission to access. Key path: N/A
- `404` Not Found (`Error`, `application/json`):

  - The endpoint you tried to access doesn’t exist. Key path: N/A
  - The channel you tried to access to search for the article doesn’t exist. Key path: `channelId`.
- `429` Too Many Requests (`Error`, `application/json`): You exceeded the number of articles that you can search for in a channel within the specific time window. The response header `<Retry-After: delay-seconds>` indicates the time in seconds you need to wait before sending a new search request.

## See Also

### Articles
- [Create an Article](./post-channels-_channelid_-articles.md)
  Publish an article to your channel.
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/get-channels-_channelid_-articles)*