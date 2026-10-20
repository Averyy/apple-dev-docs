# supportsEyedropper

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

If set to `NO` the eyedropper functionality is not supported for this color picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var supportsEyedropper: Bool { get set }
```

```objc
@property (nonatomic) BOOL supportsEyedropper;
```

## See Also

### Configuring the color picker view controller
- [var delegate: (any UIColorPickerViewControllerDelegate)?](./delegate.md)
  The delegate that receives updates about the color selection.
- [protocol UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var maximumLinearExposure: CGFloat](./maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color picker.
- [var selectedColor: UIColor](./selectedcolor.md)
  The color selected by the user.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that enables alpha value control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/supportseyedropper)*