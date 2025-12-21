# AlarmPresentationState

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the mutable content of the alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct AlarmPresentationState
```

#### Overview

This structure includes alerting, countdown, and paused states. Live Activities consists of two types of information: immutable attributes and mutable content. For example, in a live activity that’s showing the score of a soccer game the immutable attributes are the names of the teams involved in the game and the mutable content is the current score.

For alarms, immutable content is information you supply through your own processes, including information such as the tint color and the snooze button label. While mutable content comes from AlarmKit and contains information from the system, such as the alarm alert date and the alarm mode.

## Topics

### Creating an alarm state
- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](alarmpresentationstate/init(alarmid:mode:).md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](alarmpresentationstate/alarmid.md)
  The unique ID of the alarm.
- [var mode: AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.
- [AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate)*