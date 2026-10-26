# NSHighlightRect

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Highlights the specified rect by filling it with white.

**Availability**:
- macOS 10.0+ - Deprecated in 10.0

## Declaration

```c
extern void NSHighlightRect(NSRect rect);
```

#### Discussion

Highlights the rectangle referred to by `aRect`. Light gray becomes white, and white becomes light gray. This function must be called twice, once to highlight the rectangle and once to unhighlight it; the rectangle should not be left in its highlighted state. When not drawing on the screen, the compositing operation is replaced by one that fills the rectangle with light gray.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshighlightrect)*