# hasAlarms

**Framework**: EventKit  
**Kind**: property

A Boolean value that indicates whether the calendar item has alarms.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasAlarms: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the calendar item has alarms; otherwise it does not.

## See Also

- [func addAlarm(EKAlarm)](ekcalendaritem/addalarm(_:).md)
  Adds an alarm to the receiver.
- [func removeAlarm(EKAlarm)](ekcalendaritem/removealarm(_:).md)
  Removes an alarm from the calendar item.
- [var alarms: [EKAlarm]?](ekcalendaritem/alarms.md)
  The alarms associated with the calendar item, as an array of [`EKAlarm`](ekalarm.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/hasalarms)*