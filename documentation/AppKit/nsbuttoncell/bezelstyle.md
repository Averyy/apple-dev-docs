# bezelStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The appearance of the button’s border, if it has one.

**Availability**:
- macOS

## Declaration

```swift
var bezelStyle: NSButton.BezelStyle { get set }
```

```objc
@property NSBezelStyle bezelStyle;
```

#### Discussion

The value of this property is a constant that specifies the bezel style used by the button. See [`NSButton.BezelStyle`](../nsbutton/bezelstyle-swift.enum.md) for a list of possible values. If a button is borderless, the value of this property is ignored.

A button uses shading to look like it’s sticking out or pushed in. You can set the shading with the [`gradientType`](./gradienttype.md) property.

## See Also

### Managing Graphics Attributes
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the button.
- [var imageDimsWhenDisabled: Bool](./imagedimswhendisabled.md)
  A Boolean value that indicates if the button’s image and text appear “dim” when the button is disabled.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates if the button is opaque.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates if the button is transparent.
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that indicates if the button displays its border only when the pointer is over it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/bezelstyle)*