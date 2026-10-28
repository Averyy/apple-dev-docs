# titleRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle into which the menu item’s title should be drawn.

**Availability**:
- macOS

## Declaration

```swift
func titleRect(forBounds cellFrame: NSRect) -> NSRect
```

```objc
- (NSRect) titleRectForBounds:(NSRect) cellFrame;
```

## Return Value

The returned rectangle is based on `cellFrame` but encompasses only the area to be occupied by the text of the title.

## Parameters

- `cellFrame`: A rectangle that defines the bounds of the receiver.

## See Also

### Getting the Menu Item’s Drawing Rectangle
- [func keyEquivalentRect(forBounds: NSRect) -> NSRect](./keyequivalentrect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s key equivalent should be drawn.
- [func stateImageRect(forBounds: NSRect) -> NSRect](./stateimagerect%28forbounds%29.md)
  Returns the rectangle into which the menu item’s state image should be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemcell/titlerect(forbounds:))*