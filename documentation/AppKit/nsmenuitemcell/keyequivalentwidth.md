# keyEquivalentWidth

**Framework**: AppKit  
**Kind**: property

The width of the menu item’s key equivalent string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var keyEquivalentWidth: CGFloat { get }
```

#### Discussion

To set the menu item’s key equivalent, use the [`keyEquivalent`](nsmenuitem/keyequivalent.md) property of [`NSMenuItem`](nsmenuitem.md).

## See Also

- [func calcSize()](nsmenuitemcell/calcsize.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](nsmenuitemcell/needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](nsmenuitemcell/imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](nsmenuitemcell/titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var stateImageWidth: CGFloat](nsmenuitemcell/stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/keyequivalentwidth)*