# NSRectFill

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Fills the passed rectangle with the current color.

**Availability**:
- macOS

## Declaration

```c
extern void NSRectFill(NSRect rect);
```

#### Discussion

Fills `aRect` with the current color using the compositing mode [`NSCompositingOperation.copy`](./nscompositingoperation/copy.md), which fills with the current color by copying the RGBA values. Use [`NSRectFillUsingOperation`](./nsrectfillusingoperation.md) to fill specifying a compositing mode.

For more information, see [`NSCompositingOperation`](./nscompositingoperation.md).

## Parameters

- `rect`: The bounding rectangle (in the current coordinate system) in which to draw.

## See Also

### Drawing Rectangles
- [NSFrameRect](./nsframerect.md)
  Draws a bordered rectangle.
- [NSFrameRectWithWidth](./nsframerectwithwidth.md)
  Draws a bordered rectangle.
- [NSFrameRectWithWidthUsingOperation](./nsframerectwithwidthusingoperation.md)
  Draws a bordered rectangle using the specified compositing operation.
- [func NSEraseRect(NSRect)](./nseraserect%28_%29.md)
  Erases the specified rect by filling it with white.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrectfill)*