# maximumDate

**Framework**: UIKit  
**Kind**: property

The maximum date that a date picker can show.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maximumDate: Date? { get set }
```

#### Discussion

Use this property to configure the maximum date that’s selected in the date picker interface. The property contains an [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) object or `nil` (the default), which means no maximum date. This property, along with the [`minimumDate`](uidatepicker/minimumdate.md) property, lets you specify a valid date range. If the minimum date value is greater than the maximum date value, both properties are ignored. The minimum and maximum dates are also ignored in the countdown-timer mode ([`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md)).

## See Also

- [var minimumDate: Date?](uidatepicker/minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](uidatepicker/minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var countDownDuration: TimeInterval](uidatepicker/countdownduration.md)
  The value displayed by the date picker when the mode property is set to show a countdown time.
- [var roundsToMinuteInterval: Bool](uidatepicker/roundstominuteinterval.md)
  A Boolean value that determines whether the date rounds to a specific minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/maximumdate)*