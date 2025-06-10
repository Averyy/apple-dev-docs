# Alarm.Schedule.relative(_:)

**Framework**: AlarmKit  
**Kind**: case

An alarm that can repeat and fire at a time relative to the device’s current time zone.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
case relative(Alarm.Schedule.Relative)
```

#### Discussion

You can use `relative` for events which need to take into account the current time zone. For example, a wake up alarm.

## See Also

- [Alarm.Schedule.Relative](alarm/schedule-swift.enum/relative.md)
  An object that describes when an alarm alerts, relative to the device’s timezone.
- [Alarm.Schedule.fixed(_:)](alarm/schedule-swift.enum/fixed(_:).md)
  A one-shot alarm that fires at a specific time, not a time relative to the current time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative(_:))*