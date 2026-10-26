# ChannelLinks

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the links the read channel endpoint returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object ChannelLinks
```

## Mentions

- [Signing the HTTP Request](../AppleNews/signing-the-http-request.md)

## Properties

- `defaultSection` (string): The URL for this channel’s default section. Every channel has a default section, even if no others are defined.
- `self` (string): The URL at which you can read the article.

## Relationships

### Inherited By
- [ChannelResponse](./channelresponse.md)

## See Also

### Channel
- [Read Channel Information](./get-channels-_channelid_.md)
  Get details about your channel, including the name, corresponding website, and default section.
- [Read Channel Quota Information](./get-channels-_channelid_-quota.md)
  Get details about your channel’s remaining quota for sending create and update requests, the queue size, and wait time.
- [object Channel](./channel.md)
  See the fields the read channel endpoint returned.
- [object ChannelResponse](./channelresponse.md)
  See which objects make up the channel response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/channellinks)*