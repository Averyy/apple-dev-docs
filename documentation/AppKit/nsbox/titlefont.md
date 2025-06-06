# titleFont

**Framework**: AppKit  
**Kind**: property

The font object used to draw the receiver’s title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleFont: NSFont { get set }
```

#### Discussion

By default, the title is drawn using the small system font (obtained using ([`smallSystemFontSize`](nsfont/smallsystemfontsize.md) as the parameter of [`systemFont(ofSize:)`](nsfont/systemfont(ofsize:).md), both `NSFont` class methods). If the size of the new font is different from that of the old font, the content view is resized to absorb the difference.

## See Also

- [var borderRect: NSRect](nsbox/borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](nsbox/boxtype-swift.property.md)
  The receiver’s box type.
- [var borderType: NSBorderType](nsbox/bordertype.md)
  The receiver’s border type.
- [var isTransparent: Bool](nsbox/istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var title: String](nsbox/title.md)
  The receiver’s title.
- [var titlePosition: NSBox.TitlePosition](nsbox/titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/titlefont)*