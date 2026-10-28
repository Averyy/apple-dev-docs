# alarms

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The alarms associated with the calendar item, as an array of [`EKAlarm`](../ekalarm.md) objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var alarms: [EKAlarm]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<EKAlarm *> * alarms;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

## Discussion

This property is `nil` if the calendar item has no alarms.

## See Also

### Adding and Removing Alarms
- [var hasAlarms: Bool](./hasalarms.md)
  A Boolean value that indicates whether the calendar item has alarms.
- [func addAlarm(EKAlarm)](./addalarm%28_%29.md)
  Adds an alarm to the receiver.
- [func removeAlarm(EKAlarm)](./removealarm%28_%29.md)
  Removes an alarm from the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/alarms)*