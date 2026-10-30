# cascadeTopLeft(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Positions the window’s top-left to a given point.

**Availability**:
- macOS

## Declaration

```swift
func cascadeTopLeft(from topLeftPoint: NSPoint) -> NSPoint
```

```objc
- (NSPoint) cascadeTopLeftFromPoint:(NSPoint) topLeftPoint;
```

## Return Value

The point shifted from top left of the window in screen coordinates.

## Discussion

The returned point can be passed to a subsequent invocation of [`cascadeTopLeft(from:)`](./cascadetopleft%28from%29.md) to position the next window so the title bars of both windows are fully visible.

## Parameters

- `topLeftPoint`: The new top-left point, in screen coordinates, for the window. When [`NSZeroPoint`](../../Foundation/nszeropoint.md), the window is not moved, except as needed to constrain to the visible screen

## See Also

### Sizing Windows
- [var frame: NSRect](./frame.md)
  The window’s frame rectangle in screen coordinates, including the title bar.
- [func setFrameOrigin(NSPoint)](./setframeorigin%28_%29.md)
  Positions the bottom-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func setFrameTopLeftPoint(NSPoint)](./setframetopleftpoint%28_%29.md)
  Positions the top-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func constrainFrameRect(NSRect, to: NSScreen?) -> NSRect](./constrainframerect%28_,to%29.md)
  Modifies and returns a frame rectangle so that its top edge lies on a specific screen.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/cascadetopleft(from:))*