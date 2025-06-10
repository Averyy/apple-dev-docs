# Alarm.Schedule.fixed(_:)

**Framework**: AlarmKit  
**Kind**: case

A one-shot alarm that fires at a specific time, not a time relative to the current time zone.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
case fixed(Date)
```

#### Discussion

You can use `fixed` for events where the time won’t vary based on where the person is located. For example, like alerting the time of a sports game.

## See Also

- [Alarm.Schedule.Relative](alarm/schedule-swift.enum/relative.md)
  An object that describes when an alarm alerts, relative to the device’s timezone.
- [case relative(Alarm.Schedule.Relative)](alarm/schedule-swift.enum/relative(_:).md)
  An alarm that can repeat and fire at a time relative to the device’s current time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/fixed(_:))*