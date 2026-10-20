# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate that receives updates about the color selection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIColorPickerViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIColorPickerViewControllerDelegate> delegate;
```

## See Also

### Configuring the color picker view controller
- [protocol UIColorPickerViewControllerDelegate](../uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var maximumLinearExposure: CGFloat](./maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color picker.
- [var selectedColor: UIColor](./selectedcolor.md)
  The color selected by the user.
- [var supportsAlpha: Bool](./supportsalpha.md)
  A Boolean value that enables alpha value control.
- [var supportsEyedropper: Bool](./supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller/delegate)*