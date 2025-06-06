# bezelStyle

**Framework**: AppKit  
**Kind**: property

The appearance of the button’s border, if it has one.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var bezelStyle: NSButton.BezelStyle { get set }
```

#### Discussion

The value of this property is a constant that specifies the bezel style used by the button. See [`NSButton.BezelStyle`](nsbutton/bezelstyle-swift.enum.md) for a list of possible values. If a button is borderless, the value of this property is ignored.

A button uses shading to look like it’s sticking out or pushed in. You can set the shading with the [`gradientType`](nsbuttoncell/gradienttype.md) property.

## See Also

- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.
- [var imageDimsWhenDisabled: Bool](nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/bezelstyle)*