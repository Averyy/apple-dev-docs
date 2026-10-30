# constrainFrameRect(_:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies and returns a frame rectangle so that its top edge lies on a specific screen.

**Availability**:
- macOS

## Declaration

```swift
func constrainFrameRect(_ frameRect: NSRect, to screen: NSScreen?) -> NSRect
```

```objc
- (NSRect) constrainFrameRect:(NSRect) frameRect toScreen:(NSScreen *) screen;
```

## Return Value

The adjusted frame rectangle.

## Discussion

If the window is resizable and the window’s height is greater than the screen height, the rectangle’s height is adjusted to fit within the screen as well. The rectangle’s width and horizontal location are unaffected. You shouldn’t need to invoke this method yourself; it’s invoked automatically (and the modified frame is used to locate and set the size of the window) whenever a titled `NSWindow` object is placed onscreen and whenever its size is changed.

Subclasses can override this method to prevent their instances from being constrained or to constrain them differently.

## Parameters

- `frameRect`: The proposed frame rectangle to adjust.
- `screen`: The screen on which the top edge of the window’s frame is to lie.

## See Also

### Sizing Windows
- [var frame: NSRect](./frame.md)
  The window’s frame rectangle in screen coordinates, including the title bar.
- [func setFrameOrigin(NSPoint)](./setframeorigin%28_%29.md)
  Positions the bottom-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func setFrameTopLeftPoint(NSPoint)](./setframetopleftpoint%28_%29.md)
  Positions the top-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func cascadeTopLeft(from: NSPoint) -> NSPoint](./cascadetopleft%28from%29.md)
  Positions the window’s top-left to a given point.
- [var cascadingReferenceFrame: NSRect](./cascadingreferenceframe.md)
- [func setFrame(NSRect, display: Bool)](./setframe%28_,display%29.md)
  Sets the origin and size of the window’s frame rectangle according to a given frame rectangle, thereby setting its position and size onscreen.
- [func setFrame(NSRect, display: Bool, animate: Bool)](./setframe%28_,display,animate%29.md)
  Sets the origin and size of the window’s frame rectangle, with optional animation, according to a given frame rectangle, thereby setting its position and size onscreen.
- [func animationResizeTime(NSRect) -> TimeInterval](./animationresizetime%28_%29.md)
  Specifies the duration of a smooth frame-size change.
- [var aspectRatio: NSSize](./aspectratio.md)
  The window’s aspect ratio, which constrains the size of its frame rectangle to integral multiples of this ratio when the user resizes it.
- [var minSize: NSSize](./minsize.md)
  The minimum size to which the window’s frame (including its title bar) can be sized.
- [var maxSize: NSSize](./maxsize.md)
  The maximum size to which the window’s frame (including its title bar) can be sized.
- [var isZoomed: Bool](./iszoomed.md)
  A Boolean value that indicates whether the window is in a zoomed state.
- [func performZoom(Any?)](./performzoom%28_%29.md)
  This action method simulates the user clicking the zoom box by momentarily highlighting the button and then zooming the window.
- [func zoom(Any?)](./zoom%28_%29.md)
  Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).
- [var resizeFlags: NSEvent.ModifierFlags](./resizeflags.md)
  The flags field of the event record for the mouse-down event that initiated the resizing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/constrainframerect(_:to:))*