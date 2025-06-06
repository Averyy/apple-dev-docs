# titleWidth

**Framework**: AppKit  
**Kind**: property

The width of the menu item’s text, measured in points.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleWidth: CGFloat { get }
```

#### Discussion

To set the menu item’s text, use the setTitle: method of [`NSMenuItem`](nsmenuitem.md).

## See Also

- [func calcSize()](nsmenuitemcell/calcsize.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](nsmenuitemcell/needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](nsmenuitemcell/imagewidth.md)
  The width of the image associated with the menu item.
- [var keyEquivalentWidth: CGFloat](nsmenuitemcell/keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.
- [var stateImageWidth: CGFloat](nsmenuitemcell/stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/titlewidth)*