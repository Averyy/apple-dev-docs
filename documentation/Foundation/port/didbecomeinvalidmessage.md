# Port.DidBecomeInvalidMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when a port becomes invalid.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DidBecomeInvalidMessage
```

#### Overview

A [`SocketPort`](socketport.md) object can’t detect when its connection to a remote port is lost, even if the remote port is on the same machine. Therefore, it can’t invalidate itself and post this message. Instead, your app needs to detect the timeout error when sending the next message.

The [`Port`](port.md) object sending this message is no longer useful, so all receivers should unregister themselves for any notifications involving the port. The handler that receives this message should check to see which port became invalid before attempting to do anything. In particular, observers that receive all `DidBecomeInvalidMessage` instances should be aware that the system handles communication with the window server through a `Port`. If this port becomes invalid, drawing operations cause a fatal error.

Observe this message with the identifier [`didBecomeInvalid`](notificationcenter/messageidentifier/didbecomeinvalid.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`Port`](port.md).

This message interoperates with the notification [`didBecomeInvalidNotification`](port/didbecomeinvalidnotification.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](port/didbecomeinvalidmessage/init.md)
  Creates a message that indicates a port became invalid.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/didbecomeinvalidmessage)*