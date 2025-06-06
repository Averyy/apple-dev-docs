# NSDrawGroove(_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a gray-filled rectangle with a groove border.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSDrawGroove(_ rect: NSRect, _ clipRect: NSRect)
```

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw. Only those parts of   that lie within the   are actually drawn.
- `clipRect`: The clipping rectangle to use during drawing.

## See Also

- [func NSEraseRect(NSRect)](nseraserect(_:).md)
  Erases the specified rect by filling it with white.
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](nsdrawtiledrects(_:_:_:_:_:).md)
  Draws rectangles with borders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawgroove(_:_:))*