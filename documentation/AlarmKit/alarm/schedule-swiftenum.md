# Alarm.Schedule

**Framework**: AlarmKit  
**Kind**: enum

A list of all types of schedules that the framework supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum Schedule
```

## Topics

### Setting an alarm schedule
- [Alarm.Schedule.Relative](alarm/schedule-swift.enum/relative.md)
  An object that describes when an alarm alerts, relative to the device’s timezone.
- [Alarm.Schedule.fixed(_:)](alarm/schedule-swift.enum/fixed(_:).md)
  A one-shot alarm that fires at a specific time, not a time relative to the current time zone.
- [case relative(Alarm.Schedule.Relative)](alarm/schedule-swift.enum/relative(_:).md)
  An alarm that can repeat and fire at a time relative to the device’s current time zone.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var schedule: Alarm.Schedule?](alarm/schedule-swift.property.md)
  The schedule determines when the alarm alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum)*