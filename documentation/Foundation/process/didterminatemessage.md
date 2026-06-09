# Process.DidTerminateMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when a task stops operation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
struct DidTerminateMessage
```

#### Overview

Observe this message with the identifier [`didTerminate`](notificationcenter/messageidentifier/didterminate.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`Process`](process.md).

This message interoperates with the notification [`didTerminateNotification`](process/didterminatenotification.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](process/didterminatemessage/init.md)
  Creates a message about a stopped task.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/didterminatemessage)*