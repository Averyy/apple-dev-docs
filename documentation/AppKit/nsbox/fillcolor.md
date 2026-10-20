# fillColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the receiver’s background when the receiver is a custom box with a simple line border.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var fillColor: NSColor { get set }
```

```objc
@property (copy) NSColor * fillColor;
```

#### Discussion

The receiver’s fill color. It must be a custom box—that is, it has a type of [`NSBox.BoxType.custom`](./boxtype-swift.enum/custom.md)—and it must have a border style of [`NSBorderType.lineBorder`](../nsbordertype/lineborder.md).

##### Special Considerations

Functional only when the receiver’s box type ([`boxType`](./boxtype-swift.property.md)) is `NSBoxCustom` and its border type ([`borderType`](./bordertype.md)) is `NSLineBorder`.

## See Also

### Customizing
- [var borderColor: NSColor](./bordercolor.md)
  The color of the receiver’s border when the receiver is a custom box with a simple line border.
- [var borderWidth: CGFloat](./borderwidth.md)
  The width of the receiver’s border when the receiver is a custom box with a simple line border.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius of the receiver’s corners when the receiver is a custom box with a simple line border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/fillcolor)*