# Alarm.State.countdown

**Framework**: AlarmKit  
**Kind**: case

The alarm is counting down to its alert time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
case countdown
```

#### Discussion

Alarms are in this state when they are requested with a countdown duration, or when a person snoozes the alarm.

## See Also

- [Alarm.State.alerting](alarm/state-swift.enum/alerting.md)
  The alarm is currently firing.
- [Alarm.State.paused](alarm/state-swift.enum/paused.md)
  A person paused the countdown.
- [Alarm.State.scheduled](alarm/state-swift.enum/scheduled.md)
  The alarm is scheduled and ready to alert at the appropriate time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/state-swift.enum/countdown)*