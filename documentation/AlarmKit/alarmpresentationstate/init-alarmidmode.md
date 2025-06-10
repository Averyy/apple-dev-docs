# init(alarmID:mode:)

**Framework**: AlarmKit  
**Kind**: init

Creates an instance of an alarm state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)
```

## Parameters

- `alarmID`: The unique ID of the alarm.
- `mode`: The mode the alarm is in such as alerting or countdown.

## See Also

- [var alarmID: Alarm.ID](alarmpresentationstate/alarmid.md)
  The unique ID of the alarm.
- [var mode: AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.
- [AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/init(alarmid:mode:))*