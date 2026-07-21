# RCSMessage.CustomReaction

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents a custom reaction to an RCS message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct CustomReaction
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.CustomReaction.Operation)](rcsmessage/customreaction/init(targetmessageid:operation:).md)
  Creates a custom reaction instance with the message identifier and content.
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.CustomReaction.Operation, isEndToEndEncrypted: Bool)](rcsmessage/customreaction/init(targetmessageid:operation:isendtoendencrypted:).md)
  Creates a custom reaction instance with the message identifier and content.
### Instance Properties
- [var isEndToEndEncrypted: Bool](rcsmessage/customreaction/isendtoendencrypted.md)
  A Boolean value indicating whether this message is end-to-end encrypted.
- [var operation: RCSMessage.CustomReaction.Operation](rcsmessage/customreaction/operation-swift.property.md)
  The operation to perform for the custom reaction.
- [var targetMessageID: RCSMessageID](rcsmessage/customreaction/targetmessageid.md)
  The target message ID for the custom reaction.
### Enumerations
- [RCSMessage.CustomReaction.Operation](rcsmessage/customreaction/operation-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/customreaction)*