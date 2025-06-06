# selectedFontDescriptor

**Framework**: UIKit  
**Kind**: property

Information about the font family or face selected by the user in the font picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedFontDescriptor: UIFontDescriptor? { get set }
```

#### Discussion

This font descriptor does not include a size attribute, so if you want to use this descriptor as a parameter in [`init(descriptor:size:)`](uifont/init(descriptor:size:).md), you also need a size parameter greater than `0.0`.

## See Also

- [var delegate: (any UIFontPickerViewControllerDelegate)?](uifontpickerviewcontroller/delegate.md)
  The object that handles messages about the user’s interaction with a font picker.
- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/selectedfontdescriptor)*