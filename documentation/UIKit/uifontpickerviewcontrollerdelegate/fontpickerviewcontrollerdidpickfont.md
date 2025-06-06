# fontPickerViewControllerDidPickFont(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has selected a font.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func fontPickerViewControllerDidPickFont(_ viewController: UIFontPickerViewController)
```

#### Discussion

When the user picks a font, you can retrieve information about the user’s selected font from the view controller’s [`selectedFontDescriptor`](uifontpickerviewcontroller/selectedfontdescriptor.md).

## Parameters

- `viewController`: The controller for the font picker that has the user’s font selection.

## See Also

- [func fontPickerViewControllerDidCancel(UIFontPickerViewController)](uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:).md)
  Tells the delegate that the user dismissed the font picker without selecting a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:))*