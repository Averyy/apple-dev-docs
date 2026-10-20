# RCSMessage.CustomReaction

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents a custom reaction to an RCS message.

**Availability**:
- iOS 27.0+

## Declaration

```swift
struct CustomReaction
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.CustomReaction.Operation)](./customreaction/init%28targetmessageid,operation%29.md)
  Creates a custom reaction instance with the message identifier and content.
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.CustomReaction.Operation, isEndToEndEncrypted: Bool)](./customreaction/init%28targetmessageid,operation,isendtoendencrypted%29.md)
  Creates a custom reaction instance with the message identifier and content.
### Instance Properties
- [var isEndToEndEncrypted: Bool](./customreaction/isendtoendencrypted.md)
  A Boolean value indicating whether this message is end-to-end encrypted.
- [var operation: RCSMessage.CustomReaction.Operation](./customreaction/operation-swift.property.md)
  The operation to perform for the custom reaction.
- [var targetMessageID: RCSMessageID](./customreaction/targetmessageid.md)
  The target message ID for the custom reaction.
### Enumerations
- [RCSMessage.CustomReaction.Operation](./customreaction/operation-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/customreaction)*