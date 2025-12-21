# Alarm.Schedule.Relative.Time

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the hour and minute at which an alarm alerts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct Time
```

## Topics

### Creating a scheduled time
- [init(hour: Int, minute: Int)](alarm/schedule-swift.enum/relative/time-swift.struct/init(hour:minute:).md)
  Creates an instance of time.
- [var hour: Int](alarm/schedule-swift.enum/relative/time-swift.struct/hour.md)
  The hour mark the alarm alerts.
- [var minute: Int](alarm/schedule-swift.enum/relative/time-swift.struct/minute.md)
  The minute of the hour the alarm alerts.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(time: Alarm.Schedule.Relative.Time, repeats: Alarm.Schedule.Relative.Recurrence)](alarm/schedule-swift.enum/relative/init(time:repeats:).md)
  Creates an alarm that alerts at a specific 


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/time-swift.struct)*