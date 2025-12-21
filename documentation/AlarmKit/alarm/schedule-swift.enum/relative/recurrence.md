# Alarm.Schedule.Relative.Recurrence

**Framework**: AlarmKit  
**Kind**: enum

Describes the cadence at which an alarm will repeat, if any.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum Recurrence
```

## Topics

### Recurring alarms
- [Alarm.Schedule.Relative.Recurrence.never](alarm/schedule-swift.enum/relative/recurrence/never.md)
  An alarm that never repeats.
- [Alarm.Schedule.Relative.Recurrence.weekly(_:)](alarm/schedule-swift.enum/relative/recurrence/weekly(_:).md)
  An alarm that repeats weekly, on the specified day.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var repeats: Alarm.Schedule.Relative.Recurrence](alarm/schedule-swift.enum/relative/repeats.md)
  The cadence at which the alarm repeats, if any.
- [var time: Alarm.Schedule.Relative.Time](alarm/schedule-swift.enum/relative/time-swift.property.md)
  The hour and minute at which the alarm alerts, relative to the device’s current timezone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/recurrence)*