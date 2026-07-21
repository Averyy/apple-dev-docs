# RCSMessage.Reaction

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents a reaction to an RCS message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct Reaction
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.Reaction.Operation)](rcsmessage/reaction/init(targetmessageid:operation:).md)
  Creates a reaction instance with the message identifier and content.
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.Reaction.Operation, isEndToEndEncrypted: Bool)](rcsmessage/reaction/init(targetmessageid:operation:isendtoendencrypted:).md)
  Creates a reaction instance with the message identifier and content.
### Instance Properties
- [var isEndToEndEncrypted: Bool](rcsmessage/reaction/isendtoendencrypted.md)
  A Boolean value indicating whether this message is end-to-end encrypted.
- [var operation: RCSMessage.Reaction.Operation](rcsmessage/reaction/operation-swift.property.md)
  The operation to perform for the reaction.
- [var targetMessageID: RCSMessageID](rcsmessage/reaction/targetmessageid.md)
  The target message ID for the reaction.
### Enumerations
- [RCSMessage.Reaction.Operation](rcsmessage/reaction/operation-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/reaction)*