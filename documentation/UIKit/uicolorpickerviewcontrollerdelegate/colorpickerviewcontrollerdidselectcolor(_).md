# colorPickerViewControllerDidSelectColor(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the user selects a color.

**Availability**:
- iOS 14.0+ - Deprecated in 15.0
- iPadOS 14.0+ - Deprecated in 15.0
- Mac Catalyst 14.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`colorPickerViewController(_:didSelect:continuously:)`](./colorpickerviewcontroller%28_,didselect,continuously%29.md) instead.

## Declaration

```swift
optional func colorPickerViewControllerDidSelectColor(_ viewController: UIColorPickerViewController)
```

```objc
- (void) colorPickerViewControllerDidSelectColor:(UIColorPickerViewController *) viewController;
```

## Parameters

- `viewController`: The view controller that receives the color change.

## See Also

### Handling color picker activity
- [func colorPickerViewControllerDidFinish(UIColorPickerViewController)](./colorpickerviewcontrollerdidfinish%28_%29.md)
  Informs the delegate that the user dismissed the color picker.
- [func colorPickerViewController(UIColorPickerViewController, didSelect: UIColor, continuously: Bool)](./colorpickerviewcontroller%28_,didselect,continuously%29.md)
  Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor(_:))*