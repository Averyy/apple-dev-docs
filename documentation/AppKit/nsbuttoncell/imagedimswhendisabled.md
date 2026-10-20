# imageDimsWhenDisabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.

**Availability**:
- macOS

## Declaration

```swift
var imageDimsWhenDisabled: Bool { get set }
```

```objc
@property BOOL imageDimsWhenDisabled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the button’s image and text are dimmed when the button is disabled; when it is [`false`](../../Swift/false.md), the image and text are not dimmed in the disabled state. By default, all button types except [`NSSwitchButton`](../nsswitchbutton.md) and [`NSRadioButton`](../nsradiobutton.md) dim when disabled. When buttons of type [`NSSwitchButton`](../nsswitchbutton.md) and [`NSRadioButton`](../nsradiobutton.md) are disabled, only the associated text dims.

The default setting for this state is reasserted whenever you invoke [`setButtonType(_:)`](./setbuttontype%28_%29.md), so be sure to specify the button cell’s type before you set [`imageDimsWhenDisabled`](./imagedimswhendisabled.md).

## See Also

### Related Documentation
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
### Managing Graphics Attributes
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/imagedimswhendisabled)*