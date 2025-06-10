# delegate

**Framework**: UIKit  
**Kind**: property

The delegate that receives updates about the color selection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIColorPickerViewControllerDelegate)? { get set }
```

## See Also

- [protocol UIColorPickerViewControllerDelegate](uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var maximumLinearExposure: CGFloat](uicolorpickerviewcontroller/maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color picker.
- [var selectedColor: UIColor](uicolorpickerviewcontroller/selectedcolor.md)
  The color selected by the user.
- [var supportsAlpha: Bool](uicolorpickerviewcontroller/supportsalpha.md)
  A Boolean value that enables alpha value control.
- [var supportsEyedropper: Bool](uicolorpickerviewcontroller/supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/delegate)*