# isAutodisplay

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window automatically displays views that need to be displayed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isAutodisplay: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window automatically displays views that need to be displayed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). If `autodisplay` is [`false`](https://developer.apple.com/documentation/Swift/false), the window or its views must be explicitly displayed.

Automatic display typically occurs on each pass through the event loop.

## See Also

- [var needsDisplay: Bool](nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [func displayIfNeeded()](nswindow/displayifneeded.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var backingLocation: NSWindow.BackingLocation](nswindow/backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var preferredBackingLocation: NSWindow.BackingLocation](nswindow/preferredbackinglocation.md)
  A Boolean value that indicates the preferred location for the window’s backing store.
- [var isOneShot: Bool](nswindow/isoneshot.md)
  A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.
- [var drawers: [NSDrawer]?](nswindow/drawers.md)
  The collection of drawers associated with the window.
- [var showsResizeIndicator: Bool](nswindow/showsresizeindicator.md)
  A Boolean value that indicates whether the window’s resize indicator is visible.
- [var isFlushWindowDisabled: Bool](nswindow/isflushwindowdisabled.md)
  A Boolean value that indicates whether the window’s flushing ability is disabled.
- [var graphicsContext: NSGraphicsContext?](nswindow/graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](nswindow/windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isautodisplay)*