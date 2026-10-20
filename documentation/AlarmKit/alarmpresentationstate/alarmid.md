# alarmID

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The unique ID of the alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var alarmID: Alarm.ID
```

## See Also

### Creating an alarm state
- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](./init%28alarmid,mode%29.md)
  Creates an instance of an alarm state.
- [var mode: AlarmPresentationState.Mode](./mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.
- [AlarmPresentationState.Mode](./mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/alarmid)*