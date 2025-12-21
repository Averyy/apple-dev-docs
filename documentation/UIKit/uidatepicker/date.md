# date

**Framework**: UIKit  
**Kind**: property

The date displayed by the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var date: Date { get set }
```

#### Discussion

Use this property to get and set the currently selected date. The default value of this property is the date when the [`UIDatePicker`](uidatepicker.md) object is created. Setting this property animates the date picker by spinning the wheels to the new date and time; if you don’t want any animation to occur when you set the date, use the [`setDate(_:animated:)`](uidatepicker/setdate(_:animated:).md) method, passing [`false`](https://developer.apple.com/documentation/Swift/false) for the `animated` parameter. This behavior of this property is undefined when the mode is set to [`UIDatePicker.Mode.countDownTimer`](uidatepicker/mode/countdowntimer.md); refer instead to the [`countDownDuration`](uidatepicker/countdownduration.md) property.

## See Also

- [var calendar: Calendar!](uidatepicker/calendar.md)
  The calendar to use for the date picker.
- [var locale: Locale?](uidatepicker/locale.md)
  The locale used by the date picker.
- [func setDate(Date, animated: Bool)](uidatepicker/setdate(_:animated:).md)
  Sets the date to display in the date picker, with an option to animate the setting.
- [var timeZone: TimeZone?](uidatepicker/timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/date)*