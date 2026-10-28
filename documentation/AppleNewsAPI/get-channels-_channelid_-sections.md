# List All Sections

**Framework**: AppleNewsAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

See a list of available sections in your channel.

**Availability**:
- Apple News API 1.0+

## Discussion

A List All Sections request returns a list of all sections for a channel. A section is a grouping of articles on a particular topic; for example, Sports, Silicon Valley, or Politics.

You create sections in News Publisher. Sections aren’t created via the API; they are set up separately in News Publisher. See [Add and manage sections](https://support.apple.com/guide/news-publisher/apdfc6a051aa) in News Publisher User Guide. Every channel has a default section, even if no other sections are defined. The default section URL is included in the [`Read Channel Information`](./get-channels-_channelid_.md) response.

### Example

**Request**:

```
GET /channels/63a75491-2c4d-3530-af91-819be8c3ace0/sections HTTP/1.1
Host: news-api.apple.com
Accept: application/json
Authorization: HHMAC; key="1e3gfc5e-e9f8-4232-a6be-17bf40edad09"; signature="mLtpym3Lgl1300t8cze9wyWOaxkRBKL3j3ztalMjgWs="; date="2015-03-05T02:49:58Z"
```

**Response**:

```json
HTTP/1.1 200 OK
Date: Thu, 05 Mar 2015 02:53:54 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
{
  "data": [
    {
      "createdAt": "2015-03-07T00:00:56Z",
      "modifiedAt": "2015-03-07T00:11:52Z",
      "id": "0a468272-356f-3b61-afa3-c4f989954180",
      "type": "section",
      "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvA",
      "links": {
        "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
        "self": "https://news-api.apple.com/sections/0a468272-356f-3b61-afa3-c4f989954180"
      },
      "name": "Main",
      "isDefault": true
    },
    {
      "createdAt": "2015-03-08T00:00:24Z",
      "modifiedAt": "2015-03-08T00:10:11Z",
      "id": "0a664711-242f-6b13-1fa1-a6f081549989",
      "type": "section",
      "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvB",
      "links": {
        "channel": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0",
        "self": "https://news-api.apple.com/sections/0a664711-242f-6b13-1fa1-a6f081549989"
      },
      "name": "Sports",
      "isDefault": false
    }
  ]
}
```

## Endpoint

`GET https://news-api.apple.com/channels/{channelId}/sections`

## Parameters

### Path Parameters

- `channelId` (string) *(required)*: The UUID of the channel. You can get your channel ID from News Publisher. See [Use your CMS with News Publisher](https://support.apple.com/guide/news-publisher/apd88c8447e6) in News Publisher User Guide.

## Responses

- `200` OK (`SectionResponse`, `application/json`): The request was successful.
- `400` Bad Request (`Error`, `application/json`):

  - `MISSING`. You didn’t include the section UUID field in the request. Key path: `articleId`.
  - `INVALID_TYPE`. The value you specified for the section is not of the correct type for that field. Key path: `articleId`
- `401` Unauthorized (`Error`, `application/json`): You didn’t include the `Authorization` header. Key path: None.
- `403` Forbidden (`Error`, `application/json`): You tried to access a channel your API key doesn’t have permission to access. Key path: None.
- `404` Not Found (`Error`, `application/json`):

  - The endpoint you tried to access doesn’t exist. Key path: None.
  - The section you tried to access doesn’t exist. Key path: `sectionId`.

## See Also

### Sections
- [Read Section Information](./get-sections-_sectionid_.md)
  Get information about the specified section, including its name, its channel, and whether it’s a default section.
- [Promote Articles in a Section](./post-sections-_sectionid_-promotedarticles.md)
  Set the list of promoted articles for the specified section.
- [object Section](./section.md)
  See the fields the section endpoints returned.
- [object SectionLinks](./sectionlinks.md)
  See the links the section endpoints returned.
- [object SectionResponse](./sectionresponse.md)
  See which objects make up the section response.
- [object PromoteArticleRequest](./promotearticlerequest.md)
  See the required field for the Promote an Article request.
- [object PromoteArticleResponse](./promotearticleresponse.md)
  See the field the Promote an Article response returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/get-channels-_channelid_-sections)*