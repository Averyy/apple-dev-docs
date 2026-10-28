# isOpaque

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the button is opaque.

**Availability**:
- macOS

## Declaration

```swift
var isOpaque: Bool { get }
```

```objc
@property (readonly, getter=isOpaque) BOOL opaque;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the button draws over every pixel in its frame. Note that a button cell is opaque only if it isn’t transparent and if it has a border. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Managing Graphics Attributes
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the button.
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var imageDimsWhenDisabled: Bool](./imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/isopaque)*