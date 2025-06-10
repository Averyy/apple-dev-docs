# init(totalCountdownDuration:previouslyElapsedDuration:startDate:fireDate:)

**Framework**: AlarmKit  
**Kind**: init

Creates an instance of a countdown.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)
```

## Parameters

- `totalCountdownDuration`: The total duration of the countdown.
- `previouslyElapsedDuration`: The amount of time that has passed. If the countdown was   never paused or resumed, the value is zero.
- `startDate`: The date that the countdown started. If the countdown was never paused, the date is when the   countdown started.
- `fireDate`: The date at which the countdown starts.

## See Also

- [var fireDate: Date](alarmpresentationstate/mode-swift.enum/countdown/firedate.md)
  The date the countdown starts.
- [var previouslyElapsedDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var startDate: Date](alarmpresentationstate/mode-swift.enum/countdown/startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](alarmpresentationstate/mode-swift.enum/countdown/totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/init(totalcountdownduration:previouslyelapsedduration:startdate:firedate:))*