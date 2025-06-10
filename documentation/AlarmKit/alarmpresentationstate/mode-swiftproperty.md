# mode

**Framework**: AlarmKit  
**Kind**: property

The specific state of the alarm, either alerting, countdown, or paused.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var mode: AlarmPresentationState.Mode
```

#### Discussion

Use `mode` to determine which mode the alarm is in, so that a widget extension can produce the appropriate UI.

## See Also

- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](alarmpresentationstate/init(alarmid:mode:).md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](alarmpresentationstate/alarmid.md)
  The unique ID of the alarm.
- [AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.property)*