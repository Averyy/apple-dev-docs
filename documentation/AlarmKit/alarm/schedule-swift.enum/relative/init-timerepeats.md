# init(time:repeats:)

**Framework**: AlarmKit  
**Kind**: init

Creates an alarm that alerts at a specific 

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
init(time: Alarm.Schedule.Relative.Time, repeats: Alarm.Schedule.Relative.Recurrence = .never)
```

## Parameters

- `time`: The time at which the alarm will alert.
- `repeats`: The cadence at which the alarm repeats, if any.

## See Also

- [Alarm.Schedule.Relative.Time](alarm/schedule-swift.enum/relative/time-swift.struct.md)
  An object that describes the hour and minute at which an alarm alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/init(time:repeats:))*