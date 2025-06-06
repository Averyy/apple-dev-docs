# fontPickerViewControllerDidCancel(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user dismissed the font picker without selecting a font.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func fontPickerViewControllerDidCancel(_ viewController: UIFontPickerViewController)
```

#### Discussion

Implement this optional method if your app needs to add custom logic when the user cancels the font picker instead of picking a font.

## Parameters

- `viewController`: The controller for the font picker that was canceled.

## See Also

- [func fontPickerViewControllerDidPickFont(UIFontPickerViewController)](uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:).md)
  Tells the delegate that the user has selected a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:))*