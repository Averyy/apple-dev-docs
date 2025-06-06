# setFrame(_:display:animate:)

**Framework**: AppKit  
**Kind**: method

Sets the origin and size of the window’s frame rectangle, with optional animation, according to a given frame rectangle, thereby setting its position and size onscreen.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrame(_ frameRect: NSRect, display displayFlag: Bool, animate animateFlag: Bool)
```

## Parameters

- `frameRect`: The frame rectangle for the window, including the title bar.
- `displayFlag`: Specifies whether the window redraws the views that need to be displayed. When   the window sends a   message down its view hierarchy, thus redrawing all views.
- `animateFlag`: Specifies whether the window performs a smooth resize.   to perform the animation, whose duration is specified by  .

## See Also

- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/framerect(forcontentrect:stylemask:).md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [var frame: NSRect](nswindow/frame.md)
  The window’s frame rectangle in screen coordinates, including the title bar.
- [func setFrameOrigin(NSPoint)](nswindow/setframeorigin(_:).md)
  Positions the bottom-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func setFrameTopLeftPoint(NSPoint)](nswindow/setframetopleftpoint(_:).md)
  Positions the top-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func constrainFrameRect(NSRect, to: NSScreen?) -> NSRect](nswindow/constrainframerect(_:to:).md)
  Modifies and returns a frame rectangle so that its top edge lies on a specific screen.
- [func cascadeTopLeft(from: NSPoint) -> NSPoint](nswindow/cascadetopleft(from:).md)
  Positions the window’s top-left to a given point.
- [func setFrame(NSRect, display: Bool)](nswindow/setframe(_:display:).md)
  Sets the origin and size of the window’s frame rectangle according to a given frame rectangle, thereby setting its position and size onscreen.
- [func animationResizeTime(NSRect) -> TimeInterval](nswindow/animationresizetime(_:).md)
  Specifies the duration of a smooth frame-size change.
- [var aspectRatio: NSSize](nswindow/aspectratio.md)
  The window’s aspect ratio, which constrains the size of its frame rectangle to integral multiples of this ratio when the user resizes it.
- [var minSize: NSSize](nswindow/minsize.md)
  The minimum size to which the window’s frame (including its title bar) can be sized.
- [var maxSize: NSSize](nswindow/maxsize.md)
  The maximum size to which the window’s frame (including its title bar) can be sized.
- [var isZoomed: Bool](nswindow/iszoomed.md)
  A Boolean value that indicates whether the window is in a zoomed state.
- [func performZoom(Any?)](nswindow/performzoom(_:).md)
  This action method simulates the user clicking the zoom box by momentarily highlighting the button and then zooming the window.
- [func zoom(Any?)](nswindow/zoom(_:).md)
  Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).
- [var resizeFlags: NSEvent.ModifierFlags](nswindow/resizeflags.md)
  The flags field of the event record for the mouse-down event that initiated the resizing session.
- [var resizeIncrements: NSSize](nswindow/resizeincrements.md)
  The window’s resizing increments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframe(_:display:animate:))*