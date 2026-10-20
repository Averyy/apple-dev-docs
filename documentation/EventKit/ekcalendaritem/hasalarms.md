# hasAlarms

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL hasAlarms;
```

#### Discussion

If [`true`](../../Swift/true.md), the calendar item has alarms; otherwise it does not.

## See Also

### Adding and Removing Alarms
- [func addAlarm(EKAlarm)](./addalarm%28_%29.md)
  Adds an alarm to the receiver.
- [func removeAlarm(EKAlarm)](./removealarm%28_%29.md)
  Removes an alarm from the calendar item.
- [var alarms: [EKAlarm]?](./alarms.md)
  The alarms associated with the calendar item, as an array of [`EKAlarm`](../ekalarm.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/hasalarms)*