# fontPickerViewControllerDidCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user dismissed the font picker without selecting a font.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func fontPickerViewControllerDidCancel(_ viewController: UIFontPickerViewController)
```

```objc
- (void) fontPickerViewControllerDidCancel:(UIFontPickerViewController *) viewController;
```

#### Discussion

Implement this optional method if your app needs to add custom logic when the user cancels the font picker instead of picking a font.

## Parameters

- `viewController`: The controller for the font picker that was canceled.

## See Also

### Receiving font picker interactions
- [func fontPickerViewControllerDidPickFont(UIFontPickerViewController)](./fontpickerviewcontrollerdidpickfont%28_%29.md)
  Tells the delegate that the user has selected a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidcancel(_:))*