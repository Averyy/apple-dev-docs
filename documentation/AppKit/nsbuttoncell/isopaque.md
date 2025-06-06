# isOpaque

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the button is opaque.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isOpaque: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the button draws over every pixel in its frame. Note that a button cell is opaque only if it isn’t transparent and if it has a border. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var backgroundColor: NSColor?](nsbuttoncell/backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.
- [var imageDimsWhenDisabled: Bool](nsbuttoncell/imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isTransparent: Bool](nsbuttoncell/istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbuttoncell/showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/isopaque)*