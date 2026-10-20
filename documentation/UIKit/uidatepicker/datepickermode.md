# datePickerMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The mode of the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var datePickerMode: UIDatePicker.Mode { get set }
```

```objc
@property (nonatomic) UIDatePickerMode datePickerMode;
```

#### Discussion

Use this property to change the type of information displayed by the date picker. It determines whether the date picker allows selection of a date, a time, both date and time, or a countdown time. The default mode is [`UIDatePicker.Mode.dateAndTime`](./mode/dateandtime.md). See [`UIDatePicker.Mode`](./mode.md) for a list of mode constants.

## See Also

### Configuring the date picker mode
- [UIDatePicker.Mode](./mode.md)
  The mode displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/datepickermode)*