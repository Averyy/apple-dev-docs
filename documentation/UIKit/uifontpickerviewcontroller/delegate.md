# delegate

**Framework**: UIKit  
**Kind**: property

The object that handles messages about the user’s interaction with a font picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIFontPickerViewControllerDelegate)? { get set }
```

## See Also

- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [var selectedFontDescriptor: UIFontDescriptor?](uifontpickerviewcontroller/selectedfontdescriptor.md)
  Information about the font family or face selected by the user in the font picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/delegate)*