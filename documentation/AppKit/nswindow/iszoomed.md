# isZoomed

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is in a zoomed state.

**Availability**:
- macOS

## Declaration

```swift
var isZoomed: Bool { get }
```

```objc
@property (readonly, getter=isZoomed) BOOL zoomed;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window is in a zoomed state; otherwise, [`false`](../../Swift/false.md).

The zoomed state of the window is determined using the following steps:

1. If the delegate or the window class implements [`windowWillUseStandardFrame(_:defaultFrame:)`](../nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md), it is invoked to obtain the zoomed frame of the window. The value of [`isZoomed`](./iszoomed.md) is then determined by whether or not the current window frame is equal to the zoomed frame.
2. If the neither the delegate nor the window class implements [`windowWillUseStandardFrame(_:defaultFrame:)`](../nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md), a default frame that nearly fits the screen is chosen. If the delegate or window class implements [`windowWillUseStandardFrame(_:defaultFrame:)`](../nswindowdelegate/windowwillusestandardframe%28_,defaultframe%29.md), it is invoked to validate the proposed zoomed frame. After the zoomed frame is validated, the value of [`isZoomed`](./iszoomed.md) is determined by whether or not the current window frame is equal to the zoomed frame.

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
- [func performZoom(Any?)](./performzoom%28_%29.md)
  This action method simulates the user clicking the zoom box by momentarily highlighting the button and then zooming the window.
- [func zoom(Any?)](./zoom%28_%29.md)
  Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).
- [var resizeFlags: NSEvent.ModifierFlags](./resizeflags.md)
  The flags field of the event record for the mouse-down event that initiated the resizing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/iszoomed)*