# Channel

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the fields the read channel endpoint returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object Channel
```

## Mentions

- [Signing the HTTP Request](../AppleNews/signing-the-http-request.md)

## Properties

- `createdAt` (date-time): The date and time the channel was created.
- `fonts` ([string]): The list of custom fonts used in the channel. This list may be empty.
- `id` (uuid): The unique identifier of the channel.
- `modifiedAt` (date-time): The date and time the channel was last modified.
- `name` (string): The name of the channel.
- `shareUrl` (string): The URL to the channel within the News app.
- `type` (string): The channel.
- `website` (string): The website that corresponds to this channel.

## Relationships

### Inherited By
- [ChannelResponse](./channelresponse.md)

## See Also

### Channel
- [Read Channel Information](./get-channels-_channelid_.md)
  Get details about your channel, including the name, corresponding website, and default section.
- [Read Channel Quota Information](./get-channels-_channelid_-quota.md)
  Get details about your channel’s remaining quota for sending create and update requests, the queue size, and wait time.
- [object ChannelLinks](./channellinks.md)
  See the links the read channel endpoint returned.
- [object ChannelResponse](./channelresponse.md)
  See which objects make up the channel response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/channel)*