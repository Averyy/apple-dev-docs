# gradientType

**Framework**: AppKit  
**Kind**: property

The gradient of the button’s border.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var gradientType: NSButton.GradientType { get set }
```

#### Discussion

The value of this property is a constant that specifies the gradient used for the button’s border. See [`NSButton.GradientType`](nsbutton/gradienttype.md) for a list of possible values.

If the button has no border, setting this property has no effect on the button’s appearance. A concave gradient is darkest in the top-left corner; a convex gradient is darkest in the bottom-right corner. Weak versus strong is how much contrast exists between the colors used in opposite corners.

> **Note**:  This property is currently unused by AppKit and has no effect.

 This property is currently unused by AppKit and has no effect.

## See Also

- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var imageDimsWhenDisabled: Bool](nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/gradienttype)*