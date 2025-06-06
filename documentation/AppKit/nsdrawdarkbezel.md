# NSDrawDarkBezel(_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a dark gray-filled rectangle with a bezel border.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSDrawDarkBezel(_ rect: NSRect, _ clipRect: NSRect)
```

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw. Only those parts of   that lie within the   are actually drawn.
- `clipRect`: The clipping rectangle to use during drawing.

## See Also

- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](nsdrawtiledrects(_:_:_:_:_:).md)
  Draws rectangles with borders.
- [func NSDrawGrayBezel(NSRect, NSRect)](nsdrawgraybezel(_:_:).md)
  Draws a gray-filled rectangle with a bezel border.
- [func NSDrawLightBezel(NSRect, NSRect)](nsdrawlightbezel(_:_:).md)
  Draws a white-filled rectangle with a bezel border.
- [func NSDrawWhiteBezel(NSRect, NSRect)](nsdrawwhitebezel(_:_:).md)
  Draws a white-filled rectangle with a bezel border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawdarkbezel(_:_:))*