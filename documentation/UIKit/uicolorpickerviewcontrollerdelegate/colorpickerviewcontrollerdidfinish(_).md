# colorPickerViewControllerDidFinish(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the user dismissed the color picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func colorPickerViewControllerDidFinish(_ viewController: UIColorPickerViewController)
```

```objc
- (void) colorPickerViewControllerDidFinish:(UIColorPickerViewController *) viewController;
```

#### Discussion

The system calls this method when the user dismisses the color picker.

You can implement this method to show additional animations alongside the dismissal animation. For interactive dismissals, use the delegate of the presentation controller that manages the color picker instead.

## Parameters

- `viewController`: The view controller that starts dismissing.

## See Also

### Handling color picker activity
- [func colorPickerViewController(UIColorPickerViewController, didSelect: UIColor, continuously: Bool)](./colorpickerviewcontroller%28_,didselect,continuously%29.md)
  Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.
- [func colorPickerViewControllerDidSelectColor(UIColorPickerViewController)](./colorpickerviewcontrollerdidselectcolor%28_%29.md)
  Informs the delegate when the user selects a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:))*