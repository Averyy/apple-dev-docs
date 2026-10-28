# stateImageWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the image used to indicate the state of the menu item.

**Availability**:
- macOS

## Declaration

```swift
var stateImageWidth: CGFloat { get }
```

```objc
@property (readonly) CGFloat stateImageWidth;
```

## Discussion

If the menu item has multiple images associated with it (to indicate any of the available states: on, off, or mixed), this property contains the width of the largest image. You can set the state images for a menu item using the setOnStateImage:, setOffStateImage:, and setMixedStateImage: methods of [`NSMenuItem`](../nsmenuitem.md).

To change the state of the cell’s menu item, use the setState: method of [`NSMenuItem`](../nsmenuitem.md).

## See Also

### Calculating the Size of a Menu Item
- [func calcSize()](./calcsize%28%29.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](./needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](./imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](./titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var keyEquivalentWidth: CGFloat](./keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/stateimagewidth)*