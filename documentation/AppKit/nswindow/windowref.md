# windowRef

**Framework**: AppKit  
**Kind**: property

The Carbon window reference associated with the window, creating one if necessary.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var windowRef: UnsafeMutableRawPointer { get }
```

#### Discussion

You can use this property to create a `WindowRef` for a window containing a Carbon control. Subsequent accesses to this property get the existing `WindowRef`. You use a `WindowRef` to create a Carbon window reference for a Cocoa window; this assists the integration of Carbon and Cocoa code and objects.

For more information see the `MacWindows.h` header file.

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
- [var graphicsContext: NSGraphicsContext?](nswindow/graphicscontext.md)
  The graphics context associated with the window for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/windowref)*