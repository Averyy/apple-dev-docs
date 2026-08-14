# TimeZone.SystemTimeZoneDidChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the system time zone changes.

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
struct SystemTimeZoneDidChangeMessage
```

#### Overview

Observe this message with the identifier [`systemTimeZoneDidChange`](notificationcenter/messageidentifier/systemtimezonedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`TimeZone`](timezone.md).

This message interoperates with the notification [`NSSystemTimeZoneDidChange`](nsnotification/name-swift.struct/nssystemtimezonedidchange.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a system time zone change
- [init(previousTimeZone: TimeZone?)](timezone/systemtimezonedidchangemessage/init(previoustimezone:).md)
  Creates a message for a change in the system time zone.
### Accessing message properties
- [var previousTimeZone: TimeZone?](timezone/systemtimezonedidchangemessage/previoustimezone.md)
  The previous system time zone, prior to the change.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/systemtimezonedidchangemessage)*