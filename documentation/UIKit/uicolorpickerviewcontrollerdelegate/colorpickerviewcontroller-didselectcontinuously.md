# colorPickerViewController(_:didSelect:continuously:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func colorPickerViewController(_ viewController: UIColorPickerViewController, didSelect color: UIColor, continuously: Bool)
```

#### Discussion

A continuous selection is always followed by a noncontinuous one when the user finishes the gesture. Apps that support undoing should update their UI for all color changes but only undo to noncontinuous color changes.

## Parameters

- `viewController`: The color picker.
- `color`: The new color.
- `continuously`: A Boolean value that indicates whether the update is part of a continuous user interaction.

## See Also

- [func colorPickerViewControllerDidFinish(UIColorPickerViewController)](uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:).md)
  Informs the delegate that the user dismissed the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:))*