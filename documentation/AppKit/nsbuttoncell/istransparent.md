# isTransparent

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the button is transparent.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isTransparent: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button is transparent, when it is [`false`](https://developer.apple.com/documentation/Swift/false), the button is not transparent. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

Setting this property redraws the button if necessary. A transparent button tracks the mouse and sends its action, but doesn’t draw. A transparent button is useful for sensitizing an area on the screen so that an action gets sent to a target when the area receives a mouse click.

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
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/istransparent)*