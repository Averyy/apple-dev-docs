# datePickerMode

**Framework**: UIKit  
**Kind**: property

The mode of the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var datePickerMode: UIDatePicker.Mode { get set }
```

#### Discussion

Use this property to change the type of information displayed by the date picker. It determines whether the date picker allows selection of a date, a time, both date and time, or a countdown time. The default mode is [`UIDatePicker.Mode.dateAndTime`](uidatepicker/mode/dateandtime.md). See [`UIDatePicker.Mode`](uidatepicker/mode.md) for a list of mode constants.

## See Also

- [UIDatePicker.Mode](uidatepicker/mode.md)
  The mode displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/datepickermode)*