# systemClockDidChange

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a change in the system clock.

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
static var systemClockDidChange: NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Date.SystemClockDidChangeMessage`](date/systemclockdidchangemessage.md).

## See Also

- [static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage>](notificationcenter/messageidentifier/calendardaychanged.md)
  An identifier for a message about a change in calendar day.
- [static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage>](notificationcenter/messageidentifier/systemtimezonedidchange.md)
  An identifier for a message about a change in the system time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/systemclockdidchange)*