# preservesContentDuringLiveResize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window tries to optimize user-initiated resize operations by preserving the content of views that have not changed.

**Availability**:
- macOS

## Declaration

```swift
var preservesContentDuringLiveResize: Bool { get set }
```

```objc
@property BOOL preservesContentDuringLiveResize;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window tries to optimize live resize operations by preserving the content of views that have not moved; otherwise, [`false`](../../Swift/false.md). By default, live-resize optimization is turned on.

When live-resize optimization is active, the window redraws only those views that moved (or do not support this optimization) during a live resize operation. You might consider disabling this optimization for the window if none of the window’s contained views can take advantage of it. Disabling the optimization for the window prevents it from checking each view to see if the optimization is supported.

See [`preservesContentDuringLiveResize`](../nsview/preservescontentduringliveresize.md) in [`NSView`](../nsview.md) for additional information on how to support this optimization.

## See Also

### Related Documentation
- [var preservesContentDuringLiveResize: Bool](../nsview/preservescontentduringliveresize.md)
  A Boolean value indicating whether the view optimizes live-resize operations by preserving content that has not moved.
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
- [func zoom(Any?)](./zoom%28_%29.md)
  Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/preservescontentduringliveresize)*