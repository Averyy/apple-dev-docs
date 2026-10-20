# Alarm.Schedule.Relative

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that describes when an alarm alerts, relative to the device’s timezone.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Relative
```

## Topics

### Creating a scheduled alarm
- [init(time: Alarm.Schedule.Relative.Time, repeats: Alarm.Schedule.Relative.Recurrence)](./relative/init%28time,repeats%29.md)
  Creates an alarm that fires at a specific time.
- [Alarm.Schedule.Relative.Time](./relative/time-swift.struct.md)
  An object that describes the hour and minute at which an alarm alerts.
### Describing an alarm
- [var repeats: Alarm.Schedule.Relative.Recurrence](./relative/repeats.md)
  The cadence at which the alarm repeats, if any.
- [var time: Alarm.Schedule.Relative.Time](./relative/time-swift.property.md)
  The hour and minute at which the alarm alerts, relative to the device’s current timezone.
- [Alarm.Schedule.Relative.Recurrence](./relative/recurrence.md)
  Describes the cadence at which an alarm will repeat, if any.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Setting an alarm schedule
- [Alarm.Schedule.fixed(_:)](./fixed%28_%29.md)
  A one-shot alarm that fires at a specific time, not a time relative to the current time zone.
- [case relative(Alarm.Schedule.Relative)](./relative%28_%29.md)
  An alarm that can repeat and fire at a time relative to the device’s current time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative)*