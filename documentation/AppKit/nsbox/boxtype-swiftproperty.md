# boxType

**Framework**: AppKit  
**Kind**: property

The receiver’s box type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var boxType: NSBox.BoxType { get set }
```

#### Discussion

A constant describing the type of box. These constants are described in [`NSBox.BoxType`](nsbox/boxtype-swift.enum.md). By default, the box type of an `NSBox` is `NSBoxPrimary`.

## See Also

- [var borderRect: NSRect](nsbox/borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var borderType: NSBorderType](nsbox/bordertype.md)
  The receiver’s border type.
- [var isTransparent: Bool](nsbox/istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var title: String](nsbox/title.md)
  The receiver’s title.
- [var titleFont: NSFont](nsbox/titlefont.md)
  The font object used to draw the receiver’s title.
- [var titlePosition: NSBox.TitlePosition](nsbox/titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/boxtype-swift.property)*