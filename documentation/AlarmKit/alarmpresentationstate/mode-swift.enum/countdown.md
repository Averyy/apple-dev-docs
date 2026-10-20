# AlarmPresentationState.Mode.Countdown

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that specifies a countdown is in progress.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Countdown
```

## Topics

### Creating a countdown
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](./countdown/init%28totalcountdownduration,previouslyelapsedduration,startdate,firedate%29.md)
  Creates an instance of a countdown.
- [var fireDate: Date](./countdown/firedate.md)
  The date the countdown starts.
- [var previouslyElapsedDuration: TimeInterval](./countdown/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var startDate: Date](./countdown/startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](./countdown/totalcountdownduration.md)
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

### Creating a countdown
- [case countdown(AlarmPresentationState.Mode.Countdown)](./countdown%28_%29.md)
  A mode indicating the alarm timer is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown)*