# animationResizeTime(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the duration of a smooth frame-size change.

**Availability**:
- macOS

## Declaration

```swift
func animationResizeTime(_ newFrame: NSRect) -> TimeInterval
```

```objc
- (NSTimeInterval) animationResizeTime:(NSRect) newFrame;
```

## Return Value

The duration of the frame size change.

## Discussion

Subclasses can override this method to control the total time for the frame change.

The `NSWindow` implementation uses the value from the `NSWindowResizeTime` user default as the time in seconds to resize by 150 pixels. If this value is unspecified, `NSWindowResizeTime` is 0.20 seconds (this default value may be different in different releases of macOS).

## Parameters

- `newFrame`: The frame rectangle specified in [`setFrame(_:display:animate:)`](./setframe%28_,display,animate%29.md).

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
- [var resizeIncrements: NSSize](./resizeincrements.md)
  The window’s resizing increments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/animationresizetime(_:))*