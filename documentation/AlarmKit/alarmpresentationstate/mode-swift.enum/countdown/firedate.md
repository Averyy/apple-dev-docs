# fireDate

**Framework**: AlarmKit  
**Kind**: property

The date the countdown starts.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var fireDate: Date
```

#### Discussion

The alarm transitions to the `alerting` state.

## See Also

- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](alarmpresentationstate/mode-swift.enum/countdown/init(totalcountdownduration:previouslyelapsedduration:startdate:firedate:).md)
  Creates an instance of a countdown.
- [var previouslyElapsedDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var startDate: Date](alarmpresentationstate/mode-swift.enum/countdown/startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/firedate)*