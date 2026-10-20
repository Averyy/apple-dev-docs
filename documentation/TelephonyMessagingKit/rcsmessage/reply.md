# RCSMessage.Reply

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents a reply to an RCS message.

**Availability**:
- iOS 27.0+

## Declaration

```swift
struct Reply
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, content: RCSMessage.Reply.Content)](./reply/init%28targetmessageid,content%29.md)
  Creates a reply instance with the message identifier and content.
### Instance Properties
- [var content: RCSMessage.Reply.Content](./reply/content-swift.property.md)
  The content of the reply.
- [var targetMessageID: RCSMessageID](./reply/targetmessageid.md)
  The target message ID for the reply.
### Enumerations
- [RCSMessage.Reply.Content](./reply/content-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/reply)*