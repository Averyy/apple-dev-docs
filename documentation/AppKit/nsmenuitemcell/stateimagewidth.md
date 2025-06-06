# stateImageWidth

**Framework**: AppKit  
**Kind**: property

The width of the image used to indicate the state of the menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var stateImageWidth: CGFloat { get }
```

#### Discussion

If the menu item has multiple images associated with it (to indicate any of the available states: on, off, or mixed), this property contains the width of the largest image. You can set the state images for a menu item using the setOnStateImage:, setOffStateImage:, and setMixedStateImage: methods of [`NSMenuItem`](nsmenuitem.md).

To change the state of the cell’s menu item, use the setState: method of [`NSMenuItem`](nsmenuitem.md).

## See Also

- [func calcSize()](nsmenuitemcell/calcsize.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](nsmenuitemcell/needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](nsmenuitemcell/imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](nsmenuitemcell/titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var keyEquivalentWidth: CGFloat](nsmenuitemcell/keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/stateimagewidth)*