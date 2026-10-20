# startDate

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The date at which the countdown was mostly recently resumed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var startDate: Date
```

#### Discussion

If the countdown was never paused, the date is when the countdown started.

## See Also

### Creating a countdown
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](./init%28totalcountdownduration,previouslyelapsedduration,startdate,firedate%29.md)
  Creates an instance of a countdown.
- [var fireDate: Date](./firedate.md)
  The date the countdown starts.
- [var previouslyElapsedDuration: TimeInterval](./previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var totalCountdownDuration: TimeInterval](./totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/startdate)*