# zoom(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).

**Availability**:
- macOS

## Declaration

```swift
func zoom(_ sender: Any?)
```

```objc
- (void) zoom:(id) sender;
```

## Discussion

For more information on the standard and user states, see [`windowWillUseStandardFrame(_:defaultFrame:)`](../nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md).

Typically, the system invokes the [`zoom(_:)`](./zoom%28_%29.md) method after a user clicks the window’s zoom box, and [`performZoom(_:)`](./performzoom%28_%29.md) may also invoke [`zoom(_:)`](./zoom%28_%29.md) programmatically. It performs the following steps:

1. Invokes the [`windowWillUseStandardFrame(_:defaultFrame:)`](../nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md) method, if the delegate or the window class implements it, to obtain a “best fit” frame for the window. If neither the delegate nor the window class implements the method, [`zoom(_:)`](./zoom%28_%29.md) uses a default frame. The default frame nearly fills the current screen that contains the largest part of the window’s current frame.
2. Adjusts the resulting frame, if necessary, to fit on the current screen.
3. Compares the resulting frame to the current frame to determine whether the window’s standard frame is currently displayed. If the current frame is within a few pixels of the standard frame in size and location, the system considers it a match.
4. Determines a new frame. If the window is currently in the standard state, the new frame represents the user state, saved during a previous zoom. If the window is currently in the user state, the new frame represents the standard state, computed in step 1 above. If there’s no saved user state because there has been no previous zoom, the size and location of the window don’t change.
5. Determines whether the window currently allows zooming. By default, zooming is allowed. If the window’s delegate implements the [`windowShouldZoom(_:toFrame:)`](../nswindowdelegate/windowshouldzoom%28_,toframe%29.md) method, [`zoom(_:)`](./zoom%28_%29.md) invokes that method. If the delegate doesn’t implement the method but the window does, [`zoom(_:)`](./zoom%28_%29.md) invokes the window’s version. [`windowShouldZoom(_:toFrame:)`](../nswindowdelegate/windowshouldzoom%28_,toframe%29.md) returns [`false`](../../Swift/false.md) if zooming isn’t currently allowed.
6. If the window currently allows zooming, sets the new frame.

## Parameters

- `sender`: The object sending the message.

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
- [var resizeFlags: NSEvent.ModifierFlags](./resizeflags.md)
  The flags field of the event record for the mouse-down event that initiated the resizing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/zoom(_:))*