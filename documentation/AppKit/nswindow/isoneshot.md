# isOneShot

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isOneShot: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the window’s window device is freed when it’s removed from the screen list (that is, hidden) and another is created when it’s returned to the screen. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the window device is reused. Freeing the window device when it’s removed from the screen list can result in memory savings and performance improvement for window objects that don’t take long to display. Doing so is particularly appropriate for window objects the user might use once or twice, but not display continually.

## See Also

- [var backingLocation: NSWindow.BackingLocation](nswindow/backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var preferredBackingLocation: NSWindow.BackingLocation](nswindow/preferredbackinglocation.md)
  A Boolean value that indicates the preferred location for the window’s backing store.
- [var drawers: [NSDrawer]?](nswindow/drawers.md)
  The collection of drawers associated with the window.
- [var showsResizeIndicator: Bool](nswindow/showsresizeindicator.md)
  A Boolean value that indicates whether the window’s resize indicator is visible.
- [var isFlushWindowDisabled: Bool](nswindow/isflushwindowdisabled.md)
  A Boolean value that indicates whether the window’s flushing ability is disabled.
- [var isAutodisplay: Bool](nswindow/isautodisplay.md)
  A Boolean value that indicates whether the window automatically displays views that need to be displayed.
- [var graphicsContext: NSGraphicsContext?](nswindow/graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](nswindow/windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isoneshot)*