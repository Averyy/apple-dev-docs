# systemClockDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<Date.SystemClockDidChangeMessage>`.

#### Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Date.SystemClockDidChangeMessage`](../../date/systemclockdidchangemessage.md).

## See Also

### Identifying calendar, date, and time zone messages
- [static var calendarDayChanged: NotificationCenter.BaseMessageIdentifier<Calendar.CalendarDayChangedMessage>](./calendardaychanged.md)
  An identifier for a message about a change in calendar day.
- [static var systemTimeZoneDidChange: NotificationCenter.BaseMessageIdentifier<TimeZone.SystemTimeZoneDidChangeMessage>](./systemtimezonedidchange.md)
  An identifier for a message about a change in the system time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/systemclockdidchange)*