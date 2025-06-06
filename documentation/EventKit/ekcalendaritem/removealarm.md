# removeAlarm(_:)

**Framework**: EventKit  
**Kind**: method

Removes an alarm from the calendar item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeAlarm(_ alarm: EKAlarm)
```

## Mentions

- [Setting an alarm](setting-an-alarm.md)

## Parameters

- `alarm`: The alarm to be removed.

## See Also

- [var hasAlarms: Bool](ekcalendaritem/hasalarms.md)
  A Boolean value that indicates whether the calendar item has alarms.
- [func addAlarm(EKAlarm)](ekcalendaritem/addalarm(_:).md)
  Adds an alarm to the receiver.
- [var alarms: [EKAlarm]?](ekcalendaritem/alarms.md)
  The alarms associated with the calendar item, as an array of [`EKAlarm`](ekalarm.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/removealarm(_:))*