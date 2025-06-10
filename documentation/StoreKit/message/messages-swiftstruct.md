# Message.Messages

**Framework**: StoreKit  
**Kind**: struct

An asynchronous sequence of messages from the App Store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Messages
```

#### Overview

The `Message.Messages` structure provides a sequence of messages that the App Store sends to your app. Iterate over the contents of this structure asynchronously to retrieve each message if your app needs to delay the message.

Don’t create this structure directly. Instead, use [`messages`](message/messages-swift.type.property.md) method to retrieve the messages.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var messages: Message.Messages](message/messages-swift.type.property.md)
  The asynchronous sequence that sends a message when the App Store creates it.
- [let reason: Message.Reason](message/reason-swift.property.md)
  The reason that the App Store sends the message.
- [Message.Reason](message/reason-swift.struct.md)
  Reasons for the App Store messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/messages-swift.struct)*