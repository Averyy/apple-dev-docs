# Alarm.Schedule.Relative.Time

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that describes the hour and minute at which an alarm alerts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Time
```

## Topics

### Creating a scheduled time
- [init(hour: Int, minute: Int)](./time-swift.struct/init%28hour,minute%29.md)
  Creates an instance of time.
- [var hour: Int](./time-swift.struct/hour.md)
  The hour mark the alarm alerts.
- [var minute: Int](./time-swift.struct/minute.md)
  The minute of the hour the alarm alerts.

## Relationships

### Conforms To
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Creating a scheduled alarm
- [init(time: Alarm.Schedule.Relative.Time, repeats: Alarm.Schedule.Relative.Recurrence)](./init%28time,repeats%29.md)
  Creates an alarm that fires at a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/time-swift.struct)*