# selectedColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color selected by the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var selectedColor: UIColor { get set }
```

```objc
@property (nonatomic, strong) UIColor * selectedColor;
```

## See Also

### Configuring the color picker view controller
- [var delegate: (any UIColorPickerViewControllerDelegate)?](./delegate.md)
  The delegate that receives updates about the color selection.
- [protocol UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var maximumLinearExposure: CGFloat](./maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color picker.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that enables alpha value control.
- [var supportsEyedropper: Bool](./supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/selectedcolor)*