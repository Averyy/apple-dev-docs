# UIFontPickerViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of optional methods for receiving messages about the user’s interaction with the font picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFontPickerViewControllerDelegate : NSObjectProtocol
```

## Topics

### Receiving font picker interactions
- [func fontPickerViewControllerDidCancel(UIFontPickerViewController)](uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:).md)
  Tells the delegate that the user dismissed the font picker without selecting a font.
- [func fontPickerViewControllerDidPickFont(UIFontPickerViewController)](uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:).md)
  Tells the delegate that the user has selected a font.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITextFormattingCoordinator](uitextformattingcoordinator.md)

## See Also

- [class UIFontPickerViewController](uifontpickerviewcontroller.md)
  A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [UIFontPickerViewController.Configuration](uifontpickerviewcontroller/configuration-swift.class.md)
  The filters and display settings a font picker view controller uses to set up a font picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate)*