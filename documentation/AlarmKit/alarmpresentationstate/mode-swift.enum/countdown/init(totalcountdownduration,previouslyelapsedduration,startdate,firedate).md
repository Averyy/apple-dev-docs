# init(totalCountdownDuration:previouslyElapsedDuration:startDate:fireDate:)

**Framework**: AlarmKit  
**Kind**: init  
**Role**: Initializer

Creates an instance of a countdown.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(totalCountdownDuration: TimeInterval, previouslyElapsedDuration: TimeInterval, startDate: Date, fireDate: Date)
```

## Parameters

- `totalCountdownDuration`: The total duration of the countdown.
- `previouslyElapsedDuration`: The amount of time that has passed. If the countdown was never paused or resumed, the value is zero.
- `startDate`: The date that the countdown started. If the countdown was never paused, the date is when the countdown started.
- `fireDate`: The date at which the countdown starts.

## See Also

### Creating a countdown
- [var fireDate: Date](./firedate.md)
  The date the countdown starts.
- [var previouslyElapsedDuration: TimeInterval](./previouslyelapsedduration.md)
  The amount of time that elapsed before the most recent resumption of the countdown.
- [var startDate: Date](./startdate.md)
  The date at which the countdown was mostly recently resumed.
- [var totalCountdownDuration: TimeInterval](./totalcountdownduration.md)
  The total duration of the countdown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/countdown/init(totalcountdownduration:previouslyelapsedduration:startdate:firedate:))*