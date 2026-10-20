# RCSMessage.Reaction

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents a reaction to an RCS message.

**Availability**:
- iOS 27.0+

## Declaration

```swift
struct Reaction
```

## Topics

### Initializers
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.Reaction.Operation)](./reaction/init%28targetmessageid,operation%29.md)
  Creates a reaction instance with the message identifier and content.
- [init(targetMessageID: RCSMessageID, operation: RCSMessage.Reaction.Operation, isEndToEndEncrypted: Bool)](./reaction/init%28targetmessageid,operation,isendtoendencrypted%29.md)
  Creates a reaction instance with the message identifier and content.
### Instance Properties
- [var isEndToEndEncrypted: Bool](./reaction/isendtoendencrypted.md)
  A Boolean value indicating whether this message is end-to-end encrypted.
- [var operation: RCSMessage.Reaction.Operation](./reaction/operation-swift.property.md)
  The operation to perform for the reaction.
- [var targetMessageID: RCSMessageID](./reaction/targetmessageid.md)
  The target message ID for the reaction.
### Enumerations
- [RCSMessage.Reaction.Operation](./reaction/operation-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/reaction)*