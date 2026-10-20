# AlarmPresentationState.Mode.Paused

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that specifies the current state of the alarm has paused.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Paused
```

## Topics

### Pausing an alarm
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval)](./paused/init%28totalcountdownduration,previouslyelapsedduration%29.md)
  Creates an instance of a paused state.
- [var previouslyElapsedDuration: TimeInterval](./paused/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent pause of the countdown.
- [var totalCountdownDuration: TimeInterval](./paused/totalcountdownduration.md)
  The total duration of the countdown.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Pausing an alarm
- [case paused(AlarmPresentationState.Mode.Paused)](./paused%28_%29.md)
  A mode indicating the alarm isn’t active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/paused)*