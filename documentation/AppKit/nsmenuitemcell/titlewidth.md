# titleWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the menu item’s text, measured in points.

**Availability**:
- macOS

## Declaration

```swift
var titleWidth: CGFloat { get }
```

```objc
@property (readonly) CGFloat titleWidth;
```

#### Discussion

To set the menu item’s text, use the setTitle: method of [`NSMenuItem`](../nsmenuitem.md).

## See Also

### Calculating the Size of a Menu Item
- [func calcSize()](./calcsize%28%29.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var needsSizing: Bool](./needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](./imagewidth.md)
  The width of the image associated with the menu item.
- [var keyEquivalentWidth: CGFloat](./keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.
- [var stateImageWidth: CGFloat](./stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/titlewidth)*