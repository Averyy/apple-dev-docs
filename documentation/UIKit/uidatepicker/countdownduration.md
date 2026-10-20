# countDownDuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The value displayed by the date picker when the mode property is set to show a countdown time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var countDownDuration: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval countDownDuration;
```

#### Discussion

Use this property to get and set the currently selected value when the date picker’s mode property is set to [`UIDatePicker.Mode.countDownTimer`](./mode/countdowntimer.md). This property is of type [`TimeInterval`](../../Foundation/timeinterval.md) and therefore is measured in seconds, although the date picker displays only hours and minutes. If the mode of the date picker is not [`UIDatePicker.Mode.countDownTimer`](./mode/countdowntimer.md), this value is undefined; refer instead to the [`date`](./date.md) property. The default value is 0.0 and the maximum value is 23:59 (86,340 seconds).

## See Also

### Configuring temporal attributes
- [var maximumDate: Date?](./maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](./minimumdate.md)
  The minimum date that a date picker can show.
- [var minuteInterval: Int](./minuteinterval.md)
  The interval at which the date picker should display minutes.
- [var roundsToMinuteInterval: Bool](./roundstominuteinterval.md)
  A Boolean value that determines whether the date rounds to a specific minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/countdownduration)*