# Calendar.CalendarDayChangedMessage

**Framework**: Foundation  
**Kind**: struct

A message sent by a calendar when the system’s calendar day changes, as determined by the system calendar, locale, and time zone.

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
struct CalendarDayChangedMessage
```

#### Overview

If the device is asleep when the day changes, the calendar sends this message when the device wakes up. If the device has been asleep for multiple days, the calendar sends only one message.

Observe this message with the identifier [`calendarDayChanged`](notificationcenter/messageidentifier/calendardaychanged.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/asyncmessage/subject.md) of this message type is [`Calendar`](calendar.md).

This message interoperates with the notification [`NSCalendarDayChanged`](nsnotification/name-swift.struct/nscalendardaychanged.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a calendar day change
- [init()](calendar/calendardaychangedmessage/init.md)
  Creates a message for a change in calendar day.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/calendardaychangedmessage)*