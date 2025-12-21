# needsSizing

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the size of the menu needs to be calculated.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var needsSizing: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the next attempt to obtain size information about the menu cause the [`calcSize()`](nsmenuitemcell/calcsize().md) method to be called. When the value of the property is [`false`](https://developer.apple.com/documentation/Swift/false), the size information is obtained from the currently cached values.

Subclasses that drastically change the way a menu item is drawn can change the value of this property to update the menu item information. Other parts of your application should not need to change this property directly. The cell checks this value of this property as necessary when the content of its menu item changes.

## See Also

- [func calcSize()](nsmenuitemcell/calcsize.md)
  Calculates the minimum required width and height of the receiver’s menu item.
- [var imageWidth: CGFloat](nsmenuitemcell/imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](nsmenuitemcell/titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var keyEquivalentWidth: CGFloat](nsmenuitemcell/keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.
- [var stateImageWidth: CGFloat](nsmenuitemcell/stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/needssizing)*