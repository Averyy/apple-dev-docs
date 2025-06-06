# fillColor

**Framework**: AppKit  
**Kind**: property

The color of the receiver’s background when the receiver is a custom box with a simple line border.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
@MainActor var fillColor: NSColor { get set }
```

#### Discussion

The receiver’s fill color. It must be a custom box—that is, it has a type of [`NSBox.BoxType.custom`](nsbox/boxtype-swift.enum/custom.md)—and it must have a border style of [`NSBorderType.lineBorder`](nsbordertype/lineborder.md).

##### Special Considerations

Functional only when the receiver’s box type ([`boxType`](nsbox/boxtype-swift.property.md)) is `NSBoxCustom` and its border type ([`borderType`](nsbox/bordertype.md)) is `NSLineBorder`.

## See Also

- [var borderColor: NSColor](nsbox/bordercolor.md)
  The color of the receiver’s border when the receiver is a custom box with a simple line border.
- [var borderWidth: CGFloat](nsbox/borderwidth.md)
  The width of the receiver’s border when the receiver is a custom box with a simple line border.
- [var cornerRadius: CGFloat](nsbox/cornerradius.md)
  The radius of the receiver’s corners when the receiver is a custom box with a simple line border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/fillcolor)*