# AlarmPresentationState.Mode

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

A list of all modes the alarm can be in: either alert, countdown, or paused.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Mode
```

#### Overview

This value is sent as part of [`AlarmPresentationState`](../alarmpresentationstate.md) to the widget extension, so that it can produce the appropriate UI for the current state of the alarm.

## Topics

### Creating a countdown
- [AlarmPresentationState.Mode.Countdown](./mode-swift.enum/countdown.md)
  An object that specifies a countdown is in progress.
- [case countdown(AlarmPresentationState.Mode.Countdown)](./mode-swift.enum/countdown%28_%29.md)
  A mode indicating the alarm timer is active.
### Creating an alert
- [AlarmPresentationState.Mode.Alert](./mode-swift.enum/alert.md)
  A value that indicates the current state of an alarm.
- [case alert(AlarmPresentationState.Mode.Alert)](./mode-swift.enum/alert%28_%29.md)
  A mode indicating an alarm emits an alert.
### Pausing an alarm
- [AlarmPresentationState.Mode.Paused](./mode-swift.enum/paused.md)
  An object that specifies the current state of the alarm has paused.
- [case paused(AlarmPresentationState.Mode.Paused)](./mode-swift.enum/paused%28_%29.md)
  A mode indicating the alarm isn’t active.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an alarm state
- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](./init%28alarmid,mode%29.md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](./alarmid.md)
  The unique ID of the alarm.
- [var mode: AlarmPresentationState.Mode](./mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum)*