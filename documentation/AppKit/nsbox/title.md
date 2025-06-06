# title

**Framework**: AppKit  
**Kind**: property

The receiver’s title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var title: String { get set }
```

#### Discussion

The title of the `NSBox`. By default, a box’s title is “Title.” If the size of the new title is different from that of the old title, the content view is resized to absorb the difference.

## See Also

- [var borderRect: NSRect](nsbox/borderrect.md)
  The rectangle in which the receiver’s border is drawn.
- [var boxType: NSBox.BoxType](nsbox/boxtype-swift.property.md)
  The receiver’s box type.
- [var borderType: NSBorderType](nsbox/bordertype.md)
  The receiver’s border type.
- [var isTransparent: Bool](nsbox/istransparent.md)
  A Boolean value that indicates whether the receiver is transparent.
- [var titleFont: NSFont](nsbox/titlefont.md)
  The font object used to draw the receiver’s title.
- [var titlePosition: NSBox.TitlePosition](nsbox/titleposition-swift.property.md)
  A constant representing the title position.
- [var titleCell: Any](nsbox/titlecell.md)
  The cell used to display the receiver’s title.
- [var titleRect: NSRect](nsbox/titlerect.md)
  The rectangle in which the receiver’s title is drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/title)*