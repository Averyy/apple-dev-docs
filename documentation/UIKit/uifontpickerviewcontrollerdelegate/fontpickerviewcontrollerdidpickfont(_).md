# fontPickerViewControllerDidPickFont(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has selected a font.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func fontPickerViewControllerDidPickFont(_ viewController: UIFontPickerViewController)
```

```objc
- (void) fontPickerViewControllerDidPickFont:(UIFontPickerViewController *) viewController;
```

#### Discussion

When the user picks a font, you can retrieve information about the user’s selected font from the view controller’s [`selectedFontDescriptor`](../uifontpickerviewcontroller/selectedfontdescriptor.md).

## Parameters

- `viewController`: The controller for the font picker that has the user’s font selection.

## See Also

### Receiving font picker interactions
- [func fontPickerViewControllerDidCancel(UIFontPickerViewController)](./fontpickerviewcontrollerdidcancel%28_%29.md)
  Tells the delegate that the user dismissed the font picker without selecting a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:))*