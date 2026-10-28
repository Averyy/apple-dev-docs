# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The background color of the button.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * backgroundColor;
```

## Discussion

The background color is used only when drawing borderless buttons.

## See Also

### Managing Graphics Attributes
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [var imageDimsWhenDisabled: Bool](./imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/backgroundcolor)*