# mode

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The specific state of the alarm, either alerting, countdown, or paused.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var mode: AlarmPresentationState.Mode
```

#### Discussion

Use `mode` to determine which mode the alarm is in, so that a widget extension can produce the appropriate UI.

## See Also

### Creating an alarm state
- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](./init%28alarmid,mode%29.md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](./alarmid.md)
  The unique ID of the alarm.
- [AlarmPresentationState.Mode](./mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.property)*