# isTransparent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the button is transparent.

**Availability**:
- macOS

## Declaration

```swift
var isTransparent: Bool { get set }
```

```objc
@property (getter=isTransparent) BOOL transparent;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the button is transparent, when it is [`false`](../../Swift/false.md), the button is not transparent. The default value is [`false`](../../Swift/false.md).

Setting this property redraws the button if necessary. A transparent button tracks the mouse and sends its action, but doesn’t draw. A transparent button is useful for sensitizing an area on the screen so that an action gets sent to a target when the area receives a mouse click.

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
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/istransparent)*