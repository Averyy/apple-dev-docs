# NSFrameRectWithWidthUsingOperation

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Draws a bordered rectangle using the specified compositing operation.

**Availability**:
- macOS

## Declaration

```c
extern void NSFrameRectWithWidthUsingOperation(NSRect rect, CGFloat frameWidth, NSCompositingOperation op);
```

#### Discussion

Draws a frame around the inside of `aRect` in the current color, using the compositing operation `op`. The width is equal to `frameWidth` in the current coordinate system. Since the frame is drawn inside the rectangle, it will be visible even if drawing is clipped to the rectangle.

Because this function does not draw directly on the line, but rather inside it, it uses the current fill color (not stroke color) when drawing.

For more information, see [`NSCompositingOperation`](./nscompositingoperation.md).

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw.
- `frameWidth`: The width of the frame, specified in points.
- `op`: The compositing operation to use when drawing the frame.

## See Also

### Drawing Rectangles
- [NSFrameRect](./nsframerect.md)
  Draws a bordered rectangle.
- [NSFrameRectWithWidth](./nsframerectwithwidth.md)
  Draws a bordered rectangle.
- [func NSEraseRect(NSRect)](./nseraserect%28_%29.md)
  Erases the specified rect by filling it with white.
- [NSRectFill](./nsrectfill.md)
  Fills the passed rectangle with the current color.
- [NSRectFillList](./nsrectfilllist.md)
  Fills the rectangles in the passed list with the current fill color.
- [NSRectFillListUsingOperation](./nsrectfilllistusingoperation.md)
  Fills the rectangles in a list using the current fill color and specified compositing operation.
- [NSRectFillListWithColors](./nsrectfilllistwithcolors.md)
  Fills the rectangles in the passed list with the passed list of colors.
- [NSRectFillListWithColorsUsingOperation](./nsrectfilllistwithcolorsusingoperation.md)
  Fills the rectangles in a list using the specified colors and compositing operation.
- [NSRectFillListWithGrays](./nsrectfilllistwithgrays.md)
  Fills the rectangles in the passed list with the passed list of grays.
- [NSRectFillUsingOperation](./nsrectfillusingoperation.md)
  Fills a rectangle using the current fill color and the specified compositing operation.
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](./nsdrawtiledrects%28_,_,_,_,_%29.md)
  Draws rectangles with borders.
- [func NSDrawGroove(NSRect, NSRect)](./nsdrawgroove%28_,_%29.md)
  Draws a gray-filled rectangle with a groove border.
- [NSHighlightRect](./nshighlightrect.md)
  Highlights the specified rect by filling it with white.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsframerectwithwidthusingoperation)*