# calcSize()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Calculates the minimum required width and height of the receiver’s menu item.

**Availability**:
- macOS

## Declaration

```swift
func calcSize()
```

```objc
- (void) calcSize;
```

## Discussion

The calculated values are cached for future use. This method also calculates the sizes of individual components of the cell’s menu item and caches those values.

This method is invoked automatically when necessary. You should not need to invoke it directly.

## See Also

### Calculating the Size of a Menu Item
- [var needsSizing: Bool](./needssizing.md)
  A Boolean value indicating whether the size of the menu needs to be calculated.
- [var imageWidth: CGFloat](./imagewidth.md)
  The width of the image associated with the menu item.
- [var titleWidth: CGFloat](./titlewidth.md)
  The width of the menu item’s text, measured in points.
- [var keyEquivalentWidth: CGFloat](./keyequivalentwidth.md)
  The width of the menu item’s key equivalent string.
- [var stateImageWidth: CGFloat](./stateimagewidth.md)
  The width of the image used to indicate the state of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/calcsize())*