# keyEquivalentWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the menu item’s key equivalent string.

**Availability**:
- macOS

## Declaration

```swift
var keyEquivalentWidth: CGFloat { get }
```

```objc
@property (readonly) CGFloat keyEquivalentWidth;
```

#### Discussion

To set the menu item’s key equivalent, use the [`keyEquivalent`](../nsmenuitem/keyequivalent.md) property of [`NSMenuItem`](../nsmenuitem.md).

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
- [var stateImageWidth: CGFloat](./stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/keyequivalentwidth)*