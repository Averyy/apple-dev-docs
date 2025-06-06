# colorPickerViewControllerDidFinish(_:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate that the user dismissed the color picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func colorPickerViewControllerDidFinish(_ viewController: UIColorPickerViewController)
```

#### Discussion

The system calls this method when the user dismisses the color picker.

You can implement this method to show additional animations alongside the dismissal animation. For interactive dismissals, use the delegate of the presentation controller that manages the color picker instead.

## Parameters

- `viewController`: The view controller that starts dismissing.

## See Also

- [func colorPickerViewController(UIColorPickerViewController, didSelect: UIColor, continuously: Bool)](uicolorpickerviewcontrollerdelegate/colorpickerviewcontroller(_:didselect:continuously:).md)
  Informs the delegate when a user selects a color, indicating whether the update is part of a continuous user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontrollerdelegate/colorpickerviewcontrollerdidfinish(_:))*