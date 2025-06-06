# roundsToMinuteInterval

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the date rounds to a specific minute interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var roundsToMinuteInterval: Bool { get set }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), [`date`](uidatepicker/date.md) always rounds to the [`minuteInterval`](uidatepicker/minuteinterval.md) and only produces dates that align with the minute interval. If this property is [`false`](https://developer.apple.com/documentation/swift/false), changes to [`date`](uidatepicker/date.md) ignore the [`minuteInterval`](uidatepicker/minuteinterval.md) property.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var maximumDate: Date?](uidatepicker/maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](uidatepicker/minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](uidatepicker/minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var countDownDuration: TimeInterval](uidatepicker/countdownduration.md)
  The value displayed by the date picker when the mode property is set to show a countdown time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/roundstominuteinterval)*