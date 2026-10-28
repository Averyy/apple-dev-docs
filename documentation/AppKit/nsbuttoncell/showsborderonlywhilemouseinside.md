# showsBorderOnlyWhileMouseInside

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the button displays its border only when the pointer is over it.

**Availability**:
- macOS

## Declaration

```swift
var showsBorderOnlyWhileMouseInside: Bool { get set }
```

```objc
@property BOOL showsBorderOnlyWhileMouseInside;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md) if the button’s border is displayed only when the pointer is over the button and the button is active. When it is [`false`](../../Swift/false.md), the border continues to display when the pointer is outside of the button’s bounds.

## See Also

### Managing Graphics Attributes
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var imageDimsWhenDisabled: Bool](./imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates if the button is transparent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/showsborderonlywhilemouseinside)*