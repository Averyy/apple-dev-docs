# RCSMessage.Reply

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents a reply to an RCS message.

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
struct Reply
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, content: RCSMessage.Reply.Content)](rcsmessage/reply/init(targetmessageid:content:).md)
  Creates a reply instance with the message identifier and content.
### Instance Properties
- [var content: RCSMessage.Reply.Content](rcsmessage/reply/content-swift.property.md)
  The content of the reply.
- [var targetMessageID: RCSMessageID](rcsmessage/reply/targetmessageid.md)
  The target message ID for the reply.
### Enumerations
- [RCSMessage.Reply.Content](rcsmessage/reply/content-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/reply)*