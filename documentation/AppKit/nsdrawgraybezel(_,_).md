# NSDrawGrayBezel(_:_:)

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Draws a gray-filled rectangle with a bezel border.

**Availability**:
- macOS

## Declaration

```swift
func NSDrawGrayBezel(_ rect: NSRect, _ clipRect: NSRect)
```

```c
extern void NSDrawGrayBezel(NSRect rect, NSRect clipRect);
```

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw. Only those parts of `aRect` that lie within the `clipRect` are actually drawn.
- `clipRect`: The clipping rectangle to use during drawing.

## See Also

### Related Documentation
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](./nsdrawtiledrects%28_,_,_,_,_%29.md)
  Draws rectangles with borders.
### Drawing Bezels
- [func NSDrawDarkBezel(NSRect, NSRect)](./nsdrawdarkbezel%28_,_%29.md)
  Draws a dark gray-filled rectangle with a bezel border.
- [func NSDrawLightBezel(NSRect, NSRect)](./nsdrawlightbezel%28_,_%29.md)
  Draws a white-filled rectangle with a bezel border.
- [func NSDrawWhiteBezel(NSRect, NSRect)](./nsdrawwhitebezel%28_,_%29.md)
  Draws a white-filled rectangle with a bezel border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawgraybezel(_:_:))*