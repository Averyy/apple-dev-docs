# Read Channel Information

**Framework**: AppleNewsAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about your channel, including the name, corresponding website, and default section.

**Availability**:
- Apple News API 1.0+

## Mentions

- [Making an HTTP Request to the Apple News API](../AppleNews/making-an-http-request-to-the-apple-news-api.md)
- [Signing the HTTP Request](../AppleNews/signing-the-http-request.md)

## Discussion

Use the Read Channel Information endpoint to retrieve information about the channel, list of custom fonts used in the channel ([`Channel`](./channel.md)), and link to the channel’s default section ([`ChannelLinks`](./channellinks.md)). See [Making an HTTP Request to the Apple News API](../AppleNews/making-an-http-request-to-the-apple-news-api.md) and [Signing the HTTP Request](../AppleNews/signing-the-http-request.md) in [Apple News API Tutorial](../AppleNews/apple-news-api-tutorial.md).

You create a channel in News Publisher, not the Apple News API. See [Add or share a channel](https://support.apple.com/guide/news-publisher/apd1c0277d3e) in News Publisher User Guide.

### Example

**Request**:

```
GET /channels/63a75491-2c4d-3530-af91-819be8c3ace0 HTTP/1.1
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
  "data": {
    "createdAt": "2015-02-19T04:57:23Z",
    "modifiedAt": "2015-02-23T23:25:53Z",
    "id": "63a75491-2c4d-3530-af91-819be8c3ace0",
    "type": "channel",
    "shareUrl": "https://apple.news/ArRPpLPE9QXu3sehS0rvxvA",
    "links": {
      "defaultSection": "https://news-api.apple.com/sections/4523e2f6-89fb-4842-b9f2-46514f7ebc6b",
      "self": "https://news-api.apple.com/channels/63a75491-2c4d-3530-af91-819be8c3ace0"
    },
    "name": "My Channel",
    "website": "http://example.com"
    "fonts": [
    ]
  }
}
```

## Endpoint

`GET https://news-api.apple.com/channels/{channelId}`

## Parameters

### Path Parameters

- `channelId` (string) *(required)*: The UUID of the channel to get. You can get your channel ID from News Publisher. See [Use your CMS with News Publisher](https://support.apple.com/guide/news-publisher/apd88c8447e6) in News Publisher User Guide.

## Responses

- `200` OK (`ChannelResponse`, `application/json`): The request was successful.
- `400` Bad Request (`Error`, `application/json`):

  - `MISSING`. You didn’t include the Channel UUID field in the request. Key path: *
  - `INVALID_JSON`. The server can’t parse the JSON specified in the request as JSON. Key path: None.
  - `INVALID_TYPE`. The value you specified for `channelId` is not of the correct type for that field. Key path: `channelId`.
- `401` Unauthorized (`Error`, `application/json`): You didn’t include the `Authorization` header. Key path: None.
- `403` Forbidden (`Error`, `application/json`): You tried to access a channel your `API` `key` doesn’t have permission to access. Key path: None.
- `404` Not Found (`Error`, `application/json`):

  - The endpoint you tried to access doesn’t exist. Key path: None.
  - The channel you tried to access doesn’t exist. Key path: `channel_id.`

## See Also

### Channel
- [Read Channel Quota Information](./get-channels-_channelid_-quota.md)
  Get details about your channel’s remaining quota for sending create and update requests, the queue size, and wait time.
- [object Channel](./channel.md)
  See the fields the read channel endpoint returned.
- [object ChannelLinks](./channellinks.md)
  See the links the read channel endpoint returned.
- [object ChannelResponse](./channelresponse.md)
  See which objects make up the channel response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/get-channels-_channelid_)*