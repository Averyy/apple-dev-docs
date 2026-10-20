# stateImageRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle into which the menu item’s state image should be drawn.

**Availability**:
- macOS

## Declaration

```swift
func stateImageRect(forBounds cellFrame: NSRect) -> NSRect
```

```objc
- (NSRect) stateImageRectForBounds:(NSRect) cellFrame;
```

#### Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the menu item’s state image.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

### Getting the Menu Item’s Drawing Rectangle
- [func keyEquivalentRect(forBounds: NSRect) -> NSRect](./keyequivalentrect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s key equivalent should be drawn.
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s title should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/stateimagerect(forbounds:))*