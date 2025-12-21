# init(totalCountdownDuration:previouslyElapsedDuration:)

**Framework**: AlarmKit  
**Kind**: init

Creates an instance of a paused state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval)
```

## Parameters

- `totalCountdownDuration`: The total duration of the countdown.
- `previouslyElapsedDuration`: The amount of time that has elapsed. If the countdown was never paused or resumed, the value is zero.

## See Also

- [var previouslyElapsedDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/paused/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent pause of the countdown.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/paused/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/paused/init(totalcountdownduration:previouslyelapsedduration:))*