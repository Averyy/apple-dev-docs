# keyEquivalentRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle into which the menu item’s key equivalent should be drawn.

**Availability**:
- macOS

## Declaration

```swift
func keyEquivalentRect(forBounds cellFrame: NSRect) -> NSRect
```

```objc
- (NSRect) keyEquivalentRectForBounds:(NSRect) cellFrame;
```

## Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the key equivalent.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

### Getting the Menu Item’s Drawing Rectangle
- [func stateImageRect(forBounds: NSRect) -> NSRect](./stateimagerect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s state image should be drawn.
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s title should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/keyequivalentrect(forbounds:))*