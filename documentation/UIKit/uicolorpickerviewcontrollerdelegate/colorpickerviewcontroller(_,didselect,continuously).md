# colorPickerViewController(_:didSelect:continuously:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func colorPickerViewController(_ viewController: UIColorPickerViewController, didSelect color: UIColor, continuously: Bool)
```

```objc
- (void) colorPickerViewController:(UIColorPickerViewController *) viewController didSelectColor:(UIColor *) color continuously:(BOOL) continuously;
```

## Discussion

A continuous selection is always followed by a noncontinuous one when the user finishes the gesture. Apps that support undoing should update their UI for all color changes but only undo to noncontinuous color changes.

## Parameters

- `viewController`: The color picker.
- `color`: The new color.
- `continuously`: A Boolean value that indicates whether the update is part of a continuous user interaction.

## See Also

### Handling color picker activity
- [func colorPickerViewControllerDidFinish(UIColorPickerViewController)](./colorpickerviewcontrollerdidfinish%28_%29.md)
  Informs the delegate that the user dismissed the color picker.
- [func colorPickerViewControllerDidSelectColor(UIColorPickerViewController)](./colorpickerviewcontrollerdidselectcolor%28_%29.md)
  Informs the delegate when the user selects a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:))*