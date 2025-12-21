# imageDimsWhenDisabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var imageDimsWhenDisabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button’s image and text are dimmed when the button is disabled; when it is [`false`](https://developer.apple.com/documentation/Swift/false), the image and text are not dimmed in the disabled state. By default, all button types except [`NSSwitchButton`](nsswitchbutton.md) and [`NSRadioButton`](nsradiobutton.md) dim when disabled. When buttons of type [`NSSwitchButton`](nsswitchbutton.md) and [`NSRadioButton`](nsradiobutton.md) are disabled, only the associated text dims.

The default setting for this state is reasserted whenever you invoke [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md), so be sure to specify the button cell’s type before you set [`imageDimsWhenDisabled`](nsbuttoncell/imagedimswhendisabled.md).

## See Also

- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.
- [var isOpaque: Bool](nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/imagedimswhendisabled)*