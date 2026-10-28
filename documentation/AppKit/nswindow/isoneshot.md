# isOneShot

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: This property does not do anything and should not be used

## Declaration

```swift
var isOneShot: Bool { get set }
```

```objc
@property (getter=isOneShot) BOOL oneShot;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the window’s window device is freed when it’s removed from the screen list (that is, hidden) and another is created when it’s returned to the screen. When the value is [`false`](../../Swift/false.md), the window device is reused. Freeing the window device when it’s removed from the screen list can result in memory savings and performance improvement for window objects that don’t take long to display. Doing so is particularly appropriate for window objects the user might use once or twice, but not display continually.

## See Also

### Deprecated properties
- [var backingLocation: NSWindow.BackingLocation](./backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var preferredBackingLocation: NSWindow.BackingLocation](./preferredbackinglocation.md)
  A Boolean value that indicates the preferred location for the window’s backing store.
- [var drawers: [NSDrawer]?](./drawers.md)
  The collection of drawers associated with the window.
- [var showsResizeIndicator: Bool](./showsresizeindicator.md)
  A Boolean value that indicates whether the window’s resize indicator is visible.
- [var isFlushWindowDisabled: Bool](./isflushwindowdisabled.md)
  A Boolean value that indicates whether the window’s flushing ability is disabled.
- [var isAutodisplay: Bool](./isautodisplay.md)
  A Boolean value that indicates whether the window automatically displays views that need to be displayed.
- [var graphicsContext: NSGraphicsContext?](./graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](./windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.
- [var showsToolbarButton: Bool](./showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isoneshot)*