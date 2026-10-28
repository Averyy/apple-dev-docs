# resizeIncrements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s resizing increments.

**Availability**:
- macOS

## Declaration

```swift
var resizeIncrements: NSSize { get set }
```

```objc
@property NSSize resizeIncrements;
```

## Discussion

This property restricts the user’s ability to resize the window so the width and height change by multiples of width and height increments. As the user resizes the window, its size changes by multiples of `increments``.width` and `increments``.height`, which should be whole numbers, 1.0 or greater. Whatever the current resizing increments, you can set an `NSWindow` object’s size to any height and width programmatically.

Resize increments and aspect ratio are mutually exclusive attributes. For more information, see [`aspectRatio`](./aspectratio.md).

The [`contentResizeIncrements`](./contentresizeincrements.md) property takes precedence over this property.

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
- [func cascadeTopLeft(from: NSPoint) -> NSPoint](./cascadetopleft%28from%29.md)
  Positions the window’s top-left to a given point.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resizeincrements)*