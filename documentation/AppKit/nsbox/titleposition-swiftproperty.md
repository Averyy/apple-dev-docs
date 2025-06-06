# titlePosition

**Framework**: AppKit  
**Kind**: property

A constant representing the title position.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titlePosition: NSBox.TitlePosition { get set }
```

#### Discussion

A constant representing the position of the receiver’s title. See [`NSBox.TitlePosition`](nsbox/titleposition-swift.enum.md) for a list of these constants. If the new title position changes the size of the box’s border area, the content view is resized to absorb the difference, and the box is marked as needing redisplay.

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
- [var titleFont: NSFont](nsbox/titlefont.md)
  The font object used to draw the receiver’s title.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/titleposition-swift.property)*