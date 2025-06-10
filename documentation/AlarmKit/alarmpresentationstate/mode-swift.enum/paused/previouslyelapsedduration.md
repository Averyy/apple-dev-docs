# previouslyElapsedDuration

**Framework**: AlarmKit  
**Kind**: property

The amount of time that elapsed before the most recent pause of the countdown.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var previouslyElapsedDuration: TimeInterval
```

#### Discussion

If the countdown was never paused or resumed, the value is zero.

## See Also

- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval)](alarmpresentationstate/mode-swift.enum/paused/init(totalcountdownduration:previouslyelapsedduration:).md)
  Creates an instance of a paused state.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/paused/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/paused/previouslyelapsedduration)*