# UIColorPickerViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The delegate protocol to inform about changes in color selection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIColorPickerViewControllerDelegate : NSObjectProtocol
```

#### Overview

By implementing the [`UIColorPickerViewControllerDelegate`](uicolorpickerviewcontrollerdelegate.md) functions, your app can react to a color-selection change or the dismissal of the color picker.

## Topics

### Handling color picker activity
- [func colorPickerViewControllerDidFinish(UIColorPickerViewController)](uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:).md)
  Informs the delegate that the user dismissed the color picker.
- [func colorPickerViewController(UIColorPickerViewController, didSelect: UIColor, continuously: Bool)](uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:).md)
  Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.
### Deprecated
- [func colorPickerViewControllerDidSelectColor(UIColorPickerViewController)](uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidselectcolor(_:).md)
  Informs the delegate when the user selects a color.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIColorPickerViewController](uicolorpickerviewcontroller.md)
  A view controller that manages the interface for selecting a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate)*