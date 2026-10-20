# UIDatePickerStyle.inline

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A style indicating that the date pickers displays as an inline, editable field.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
case inline
```

```c
UIDatePickerStyleInline
```

#### Discussion

Use this style when you want to let users edit the date picker value without having to tap the label shown in the [`UIDatePickerStyle.compact`](./compact.md) style.

You can’t use this style with the [`UIDatePicker.Mode.countDownTimer`](../uidatepicker/mode/countdowntimer.md) mode.

## See Also

### Styles
- [UIDatePickerStyle.automatic](./automatic.md)
  A style indicating that the system picks the concrete style based on the current platform and date picker mode.
- [UIDatePickerStyle.compact](./compact.md)
  A style indicating that the date picker displays as a label that when tapped displays a calendar-style editor.
- [UIDatePickerStyle.wheels](./wheels.md)
  A style indicating that the date picker displays as a wheel picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepickerstyle/inline)*