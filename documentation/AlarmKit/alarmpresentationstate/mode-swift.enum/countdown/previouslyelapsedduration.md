# previouslyElapsedDuration

**Framework**: AlarmKit  
**Kind**: property

The amount of time that elapsed before the most recent resumption of the countdown.

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

- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](alarmpresentationstate/mode-swift.enum/countdown/init(totalcountdownduration:previouslyelapsedduration:startdate:firedate:).md)
  Creates an instance of a countdown.
- [var fireDate: Date](alarmpresentationstate/mode-swift.enum/countdown/firedate.md)
  The date the countdown starts.
- [var startDate: Date](alarmpresentationstate/mode-swift.enum/countdown/startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/previouslyelapsedduration)*