# Alarm.Schedule

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

A list of all types of schedules that the framework supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Schedule
```

## Topics

### Setting an alarm schedule
- [Alarm.Schedule.Relative](./schedule-swift.enum/relative.md)
  An object that describes when an alarm alerts, relative to the device’s timezone.
- [Alarm.Schedule.fixed(_:)](./schedule-swift.enum/fixed%28_%29.md)
  A one-shot alarm that fires at a specific time, not a time relative to the current time zone.
- [case relative(Alarm.Schedule.Relative)](./schedule-swift.enum/relative%28_%29.md)
  An alarm that can repeat and fire at a time relative to the device’s current time zone.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting an alarm schedule
- [var schedule: Alarm.Schedule?](./schedule-swift.property.md)
  The schedule determines when the alarm alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum)*