# previouslyElapsedDuration

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The amount of time that elapsed before the most recent pause of the countdown.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var previouslyElapsedDuration: TimeInterval
```

#### Discussion

If the countdown was never paused or resumed, the value is zero.

## See Also

### Pausing an alarm
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval)](./init%28totalcountdownduration,previouslyelapsedduration%29.md)
  Creates an instance of a paused state.
- [var totalCountdownDuration: TimeInterval](./totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/paused/previouslyelapsedduration)*