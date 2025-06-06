# countDownDuration

**Framework**: UIKit  
**Kind**: property

The value displayed by the date picker when the mode property is set to show a countdown time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var countDownDuration: TimeInterval { get set }
```

#### Discussion

Use this property to get and set the currently selected value when the date picker’s mode property is set to [`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md). This property is of type [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) and therefore is measured in seconds, although the date picker displays only hours and minutes. If the mode of the date picker is not [`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md), this value is undefined; refer instead to the [`date`](uidatepicker/date.md) property. The default value is 0.0 and the maximum value is 23:59 (86,340 seconds).

## See Also

- [var maximumDate: Date?](uidatepicker/maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](uidatepicker/minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](uidatepicker/minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var roundsToMinuteInterval: Bool](uidatepicker/roundstominuteinterval.md)
  A Boolean value that determines whether the date rounds to a specific minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/countdownduration)*