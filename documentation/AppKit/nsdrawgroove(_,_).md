# NSDrawGroove(_:_:)

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Draws a gray-filled rectangle with a groove border.

**Availability**:
- macOS

## Declaration

```swift
func NSDrawGroove(_ rect: NSRect, _ clipRect: NSRect)
```

```c
extern void NSDrawGroove(NSRect rect, NSRect clipRect);
```

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw. Only those parts of `aRect` that lie within the `clipRect` are actually drawn.
- `clipRect`: The clipping rectangle to use during drawing.

## See Also

### Drawing Rectangles
- [func NSEraseRect(NSRect)](./nseraserect%28_%29.md)
  Erases the specified rect by filling it with white.
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](./nsdrawtiledrects%28_,_,_,_,_%29.md)
  Draws rectangles with borders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawgroove(_:_:))*