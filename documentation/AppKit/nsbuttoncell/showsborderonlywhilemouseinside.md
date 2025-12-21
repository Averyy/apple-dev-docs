# showsBorderOnlyWhileMouseInside

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the button displays its border only when the pointer is over it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var showsBorderOnlyWhileMouseInside: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the button’s border is displayed only when the pointer is over the button and the button is active. When it is [`false`](https://developer.apple.com/documentation/Swift/false), the border continues to display when the pointer is outside of the button’s bounds.

## See Also

- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.
- [var imageDimsWhenDisabled: Bool](nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](nsbuttoncell/isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/showsborderonlywhilemouseinside)*