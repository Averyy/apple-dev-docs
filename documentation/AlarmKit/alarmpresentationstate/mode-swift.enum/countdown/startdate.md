# startDate

**Framework**: AlarmKit  
**Kind**: property

The date at which the countdown was mostly recently resumed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var startDate: Date
```

#### Discussion

If the countdown was never paused, the date is when the countdown started.

## See Also

- [init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)](alarmpresentationstate/mode-swift.enum/countdown/init(totalcountdownduration:previouslyelapsedduration:startdate:firedate:).md)
  Creates an instance of a countdown.
- [var fireDate: Date](alarmpresentationstate/mode-swift.enum/countdown/firedate.md)
  The date the countdown starts.
- [var previouslyElapsedDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/startdate)*