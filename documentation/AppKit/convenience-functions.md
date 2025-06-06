# Convenience Functions

**Framework**: AppKit

Draw rectangles and other primitive shapes using these convenience functions.

## Topics

### Drawing Rectangles
- [func NSEraseRect(NSRect)](nseraserect(_:).md)
  Erases the specified rect by filling it with white.
- [func NSDrawTiledRects(NSRect, NSRect, UnsafePointer<NSRectEdge>, UnsafePointer<CGFloat>, Int) -> NSRect](nsdrawtiledrects(_:_:_:_:_:).md)
  Draws rectangles with borders.
- [func NSDrawGroove(NSRect, NSRect)](nsdrawgroove(_:_:).md)
  Draws a gray-filled rectangle with a groove border.
### Drawing Bezels
- [func NSDrawDarkBezel(NSRect, NSRect)](nsdrawdarkbezel(_:_:).md)
  Draws a dark gray-filled rectangle with a bezel border.
- [func NSDrawGrayBezel(NSRect, NSRect)](nsdrawgraybezel(_:_:).md)
  Draws a gray-filled rectangle with a bezel border.
- [func NSDrawLightBezel(NSRect, NSRect)](nsdrawlightbezel(_:_:).md)
  Draws a white-filled rectangle with a bezel border.
- [func NSDrawWhiteBezel(NSRect, NSRect)](nsdrawwhitebezel(_:_:).md)
  Draws a white-filled rectangle with a bezel border.
### Drawing Backgrounds
- [func NSDrawButton(NSRect, NSRect)](nsdrawbutton(_:_:).md)
  Draws a gray-filled rectangle representing a user-interface button.
- [func NSDrawWindowBackground(NSRect)](nsdrawwindowbackground(_:).md)
  Draws the window’s default background pattern into the specified rectangle of the currently focused view.
### Drawing Multipart Images
- [func NSDrawNinePartImage(NSRect, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSImage?, NSCompositingOperation, CGFloat, Bool)](nsdrawninepartimage(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a nine-part tiled image.
- [func NSDrawThreePartImage(NSRect, NSImage?, NSImage?, NSImage?, Bool, NSCompositingOperation, CGFloat, Bool)](nsdrawthreepartimage(_:_:_:_:_:_:_:_:).md)
  Draws a three-part tiled image.
### Drawing Focus Rings
- [func set()](nsfocusringplacement/set.md)
  Specifies how the system draws the focus ring.
- [enum NSFocusRingPlacement](nsfocusringplacement.md)
  Constants that indicate how the system draws the focus ring.
- [enum NSFocusRingType](nsfocusringtype.md)
  Constants that describe the style of the focus ring.

## See Also

- [class NSBezierPath](nsbezierpath.md)
  An object that can create paths using PostScript-style commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/convenience-functions)*