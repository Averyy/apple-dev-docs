# maximumLinearExposure

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum exposure to apply to a color when returned by the color picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var maximumLinearExposure: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat maximumLinearExposure;
```

## See Also

### Configuring the color picker view controller
- [var delegate: (any UIColorPickerViewControllerDelegate)?](./delegate.md)
  The delegate that receives updates about the color selection.
- [protocol UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var selectedColor: UIColor](./selectedcolor.md)
  The color selected by the user.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that enables alpha value control.
- [var supportsEyedropper: Bool](./supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/maximumlinearexposure)*