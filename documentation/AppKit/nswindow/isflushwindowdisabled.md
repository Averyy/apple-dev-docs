# isFlushWindowDisabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window’s flushing ability is disabled.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isFlushWindowDisabled: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window’s flushing ability has been disabled; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func disableFlushing()](nswindow/disableflushing.md)
  Disables the [`flush()`](nswindow/flush().md) method for the window.
- [func enableFlushing()](nswindow/enableflushing.md)
  Reenables the [`flush()`](nswindow/flush().md) method for the window after it was disabled through a previous [`disableFlushing()`](nswindow/disableflushing().md) message.
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
- [var isAutodisplay: Bool](nswindow/isautodisplay.md)
  A Boolean value that indicates whether the window automatically displays views that need to be displayed.
- [var graphicsContext: NSGraphicsContext?](nswindow/graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](nswindow/windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isflushwindowdisabled)*