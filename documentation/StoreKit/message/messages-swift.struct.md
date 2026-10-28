# Message.Messages

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

The `Message.Messages` structure provides a sequence of messages that the App Store sends to your app. Iterate over the contents of this structure asynchronously to retrieve each message if your app needs to delay the message.

Don’t create this structure directly. Instead, use [`messages`](./messages-swift.type.property.md) method to retrieve the messages.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting messages and message reasons
- [static var messages: Message.Messages](./messages-swift.type.property.md)
  The asynchronous sequence that sends a message when the App Store creates it.
- [let reason: Message.Reason](./reason-swift.property.md)
  The reason that the App Store sends the message.
- [Message.Reason](./reason-swift.struct.md)
  Reasons for the App Store messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/messages-swift.struct)*