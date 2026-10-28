# preferredBackingLocation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the preferred location for the window’s backing store.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: This property does not do anything and should not be used

## Declaration

```swift
var preferredBackingLocation: NSWindow.BackingLocation { get set }
```

```objc
@property NSWindowBackingLocation preferredBackingLocation;
```

## Discussion

See [`NSWindow.BackingLocation`](./backinglocation-swift.enum.md) for possible values. It’s recommended that you set this property only when optimizing for performance.

## See Also

### Deprecated properties
- [var backingLocation: NSWindow.BackingLocation](./backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var isOneShot: Bool](./isoneshot.md)
  A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/preferredbackinglocation)*