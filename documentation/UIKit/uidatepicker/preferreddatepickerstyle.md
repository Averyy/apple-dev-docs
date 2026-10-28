# preferredDatePickerStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred style of the date picker.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var preferredDatePickerStyle: UIDatePickerStyle { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIDatePickerStyle preferredDatePickerStyle;
```

## Discussion

Use this property to specify the display style that you prefer. If the style changes, the date picker may generate a layout pass to update the display.

The default style is [`UIDatePickerStyle.automatic`](../uidatepickerstyle/automatic.md). For a list of styles, see [`UIDatePickerStyle`](../uidatepickerstyle.md).

## See Also

### Configuring the date picker style
- [var datePickerStyle: UIDatePickerStyle](./datepickerstyle.md)
  The current style of the date picker.
- [enum UIDatePickerStyle](../uidatepickerstyle.md)
  Styles that determine the appearance of a date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/preferreddatepickerstyle)*