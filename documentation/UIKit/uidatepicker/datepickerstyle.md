# datePickerStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current style of the date picker.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var datePickerStyle: UIDatePickerStyle { get }
```

```objc
@property (nonatomic, assign, readonly) UIDatePickerStyle datePickerStyle;
```

## Discussion

This property always returns a concrete style, never [`UIDatePickerStyle.automatic`](../uidatepickerstyle/automatic.md).

## See Also

### Configuring the date picker style
- [var preferredDatePickerStyle: UIDatePickerStyle](./preferreddatepickerstyle.md)
  The preferred style of the date picker.
- [enum UIDatePickerStyle](../uidatepickerstyle.md)
  Styles that determine the appearance of a date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/datepickerstyle)*