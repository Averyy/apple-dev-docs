# graphicsContext

**Framework**: AppKit  
**Kind**: property

The graphics context associated with the window for the current thread.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var graphicsContext: NSGraphicsContext? { get }
```

## See Also

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
- [var isAutodisplay: Bool](nswindow/isautodisplay.md)
  A Boolean value that indicates whether the window automatically displays views that need to be displayed.
- [var windowRef: UnsafeMutableRawPointer](nswindow/windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/graphicscontext)*