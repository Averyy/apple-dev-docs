# Convenience Functions

**Framework**: AppKit  
**Role**: API Collection

Draw rectangles and other primitive shapes using these convenience functions.

## Topics

### Drawing Rectangles
- [func NSEraseRect(NSRect)](./nseraserect%28_%29.md)
  Erases the specified rect by filling it with white.
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](./nsdrawtiledrects%28_,_,_,_,_%29.md)
  Draws rectangles with borders.
- [func NSDrawGroove(NSRect, NSRect)](./nsdrawgroove%28_,_%29.md)
  Draws a gray-filled rectangle with a groove border.
- [NSFrameRect](./nsframerect.md)
  Draws a bordered rectangle.
- [NSFrameRectWithWidth](./nsframerectwithwidth.md)
  Draws a bordered rectangle.
- [NSFrameRectWithWidthUsingOperation](./nsframerectwithwidthusingoperation.md)
  Draws a bordered rectangle using the specified compositing operation.
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
- [NSHighlightRect](./nshighlightrect.md)
  Highlights the specified rect by filling it with white.
### Drawing Bezels
- [func NSDrawDarkBezel(NSRect, NSRect)](./nsdrawdarkbezel%28_,_%29.md)
  Draws a dark gray-filled rectangle with a bezel border.
- [func NSDrawGrayBezel(NSRect, NSRect)](./nsdrawgraybezel%28_,_%29.md)
  Draws a gray-filled rectangle with a bezel border.
- [func NSDrawLightBezel(NSRect, NSRect)](./nsdrawlightbezel%28_,_%29.md)
  Draws a white-filled rectangle with a bezel border.
- [func NSDrawWhiteBezel(NSRect, NSRect)](./nsdrawwhitebezel%28_,_%29.md)
  Draws a white-filled rectangle with a bezel border.
### Drawing Backgrounds
- [func NSDrawButton(NSRect, NSRect)](./nsdrawbutton%28_,_%29.md)
  Draws a gray-filled rectangle representing a user-interface button.
- [func NSDrawWindowBackground(NSRect)](./nsdrawwindowbackground%28_%29.md)
  Draws the window’s default background pattern into the specified rectangle of the currently focused view.
### Drawing Multipart Images
- [func NSDrawNinePartImage(NSRect, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSCompositingOperation, CGFloat, Bool)](./nsdrawninepartimage%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Draws a nine-part tiled image.
- [func NSDrawThreePartImage(NSRect, NSImage?, NSImage?, NSImage?, Bool, NSCompositingOperation, CGFloat, Bool)](./nsdrawthreepartimage%28_,_,_,_,_,_,_,_%29.md)
  Draws a three-part tiled image.
### Drawing Focus Rings
- [func set()](./nsfocusringplacement/set%28%29.md)
  Specifies how the system draws the focus ring.
- [enum NSFocusRingPlacement](./nsfocusringplacement.md)
  Constants that indicate how the system draws the focus ring.
- [enum NSFocusRingType](./nsfocusringtype.md)
  Constants that describe the style of the focus ring.
### Clipping Rectangles
- [NSRectClip](./nsrectclip.md)
  Modifies the current clipping path by intersecting it with the passed rect.
- [NSRectClipList](./nsrectcliplist.md)
  Modifies the current clipping path by intersecting it with the passed rect.

## See Also

### Shapes and Paths
- [class NSBezierPath](./nsbezierpath.md)
  An object that can create paths using PostScript-style commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/convenience-functions)*