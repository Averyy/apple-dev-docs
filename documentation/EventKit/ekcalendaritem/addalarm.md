# addAlarm(_:)

**Framework**: EventKit  
**Kind**: method

Adds an alarm to the receiver.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addAlarm(_ alarm: EKAlarm)
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)
- [Setting an alarm](setting-an-alarm.md)

## Parameters

- `alarm`: The alarm to be added.

## See Also

- [var hasAlarms: Bool](ekcalendaritem/hasalarms.md)
  A Boolean value that indicates whether the calendar item has alarms.
- [func removeAlarm(EKAlarm)](ekcalendaritem/removealarm(_:).md)
  Removes an alarm from the calendar item.
- [var alarms: [EKAlarm]?](ekcalendaritem/alarms.md)
  The alarms associated with the calendar item, as an array of [`EKAlarm`](ekalarm.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/addalarm(_:))*