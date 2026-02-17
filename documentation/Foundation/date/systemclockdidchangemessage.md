# Date.SystemClockDidChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the system clock changes.

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
struct SystemClockDidChangeMessage
```

#### Overview

Various events can initiate this message, such as a call to `settimeofday(_:_:)`, or if the person using the device changes values in Settings.

Observe this message with the identifier [`systemClockDidChange`](notificationcenter/messageidentifier/systemclockdidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`Date`](date.md).

This message interoperates with the notification [`NSSystemClockDidChange`](nsnotification/name-swift.struct/nssystemclockdidchange.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a system clock change
- [init()](date/systemclockdidchangemessage/init.md)
  Creates a message for a change in the system clock.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/systemclockdidchangemessage)*