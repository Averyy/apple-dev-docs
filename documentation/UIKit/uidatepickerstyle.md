# UIDatePickerStyle

**Framework**: UIKit  
**Kind**: enum

Styles that determine the appearance of a date picker.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
enum UIDatePickerStyle
```

#### Overview

A date picker style determines how your app displays the date picker value and its editor. For instance, a date picker with a [`datePickerMode`](uidatepicker/datepickermode.md) of [`UIDatePicker.Mode.dateAndTime`](uidatepicker/mode/dateandtime.md) and [`datePickerStyle`](uidatepicker/datepickerstyle.md) of [`UIDatePickerStyle.compact`](uidatepickerstyle/compact.md) displays the date picker’s value as a label that the user can tap to view a calendar-style editor. On the other hand, the same date picker using the [`UIDatePickerStyle.inline`](uidatepickerstyle/inline.md) style displays a view that lets the user edit the value without having to tap the label shown in the [`UIDatePickerStyle.compact`](uidatepickerstyle/compact.md) style.

## Topics

### Styles
- [UIDatePickerStyle.automatic](uidatepickerstyle/automatic.md)
  A style indicating that the system picks the concrete style based on the current platform and date picker mode.
- [UIDatePickerStyle.compact](uidatepickerstyle/compact.md)
  A style indicating that the date picker displays as a label that when tapped displays a calendar-style editor.
- [UIDatePickerStyle.inline](uidatepickerstyle/inline.md)
  A style indicating that the date pickers displays as an inline, editable field.
- [UIDatePickerStyle.wheels](uidatepickerstyle/wheels.md)
  A style indicating that the date picker displays as a wheel picker.
### Initializers
- [init?(rawValue: Int)](uidatepickerstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var datePickerStyle: UIDatePickerStyle](uidatepicker/datepickerstyle.md)
  The current style of the date picker.
- [var preferredDatePickerStyle: UIDatePickerStyle](uidatepicker/preferreddatepickerstyle.md)
  The preferred style of the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepickerstyle)*