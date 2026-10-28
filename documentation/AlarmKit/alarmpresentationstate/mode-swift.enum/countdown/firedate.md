# fireDate

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The date the countdown starts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var fireDate: Date
```

## Discussion

The alarm transitions to the `alerting` state.

## See Also

### Creating a countdown
- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](./init%28totalcountdownduration,previouslyelapsedduration,startdate,firedate%29.md)
  Creates an instance of a countdown.
- [var previouslyElapsedDuration: TimeInterval](./previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var startDate: Date](./startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](./totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/firedate)*