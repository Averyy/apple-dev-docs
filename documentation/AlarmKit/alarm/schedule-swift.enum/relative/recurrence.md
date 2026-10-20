# Alarm.Schedule.Relative.Recurrence

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

Describes the cadence at which an alarm will repeat, if any.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Recurrence
```

## Topics

### Recurring alarms
- [Alarm.Schedule.Relative.Recurrence.never](./recurrence/never.md)
  An alarm that never repeats.
- [Alarm.Schedule.Relative.Recurrence.weekly(_:)](./recurrence/weekly%28_%29.md)
  An alarm that repeats weekly, on the specified day.

## Relationships

### Conforms To
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Describing an alarm
- [var repeats: Alarm.Schedule.Relative.Recurrence](./repeats.md)
  The cadence at which the alarm repeats, if any.
- [var time: Alarm.Schedule.Relative.Time](./time-swift.property.md)
  The hour and minute at which the alarm alerts, relative to the device’s current timezone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/recurrence)*