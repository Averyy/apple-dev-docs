# previouslyElapsedDuration

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The amount of time that elapsed before the most recent resumption of the countdown.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var previouslyElapsedDuration: TimeInterval
```

## Discussion

If the countdown was never paused or resumed, the value is zero.

## See Also

### Creating a countdown
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](./init%28totalcountdownduration,previouslyelapsedduration,startdate,firedate%29.md)
  Creates an instance of a countdown.
- [var fireDate: Date](./firedate.md)
  The date the countdown starts.
- [var startDate: Date](./startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](./totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/previouslyelapsedduration)*