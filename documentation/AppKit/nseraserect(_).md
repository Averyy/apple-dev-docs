# NSEraseRect(_:)

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Erases the specified rect by filling it with white.

**Availability**:
- macOS

## Declaration

```swift
func NSEraseRect(_ rect: NSRect)
```

```c
extern void NSEraseRect(NSRect rect);
```

#### Discussion

This function fills the specified rectangle with white. It does not alter the current color.

## Parameters

- `rect`: The rectangle (in the current coordinate system) defining the area to erase.

## See Also

### Drawing Rectangles
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](./nsdrawtiledrects%28_,_,_,_,_%29.md)
  Draws rectangles with borders.
- [func NSDrawGroove(NSRect, NSRect)](./nsdrawgroove%28_,_%29.md)
  Draws a gray-filled rectangle with a groove border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseraserect(_:))*