# datePickerStyle

**Framework**: UIKit  
**Kind**: property

The current style of the date picker.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var datePickerStyle: UIDatePickerStyle { get }
```

#### Discussion

This property always returns a concrete style, never [`UIDatePickerStyle.automatic`](uidatepickerstyle/automatic.md).

## See Also

- [var preferredDatePickerStyle: UIDatePickerStyle](uidatepicker/preferreddatepickerstyle.md)
  The preferred style of the date picker.
- [enum UIDatePickerStyle](uidatepickerstyle.md)
  Styles that determine the appearance of a date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/datepickerstyle)*