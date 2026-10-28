# showsToolbarButton

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar control button is currently displayed.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: This property has no effect

## Declaration

```swift
var showsToolbarButton: Bool { get set }
```

```objc
@property BOOL showsToolbarButton;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the standard toolbar button is currently displayed; otherwise, [`false`](../../Swift/false.md). When clicked, the toolbar control button shows or hides a window’s toolbar. The toolbar control button appears in a window’s title bar. If the window does not have a toolbar, this property has no effect.

## See Also

### Deprecated properties
- [var backingLocation: NSWindow.BackingLocation](./backinglocation-swift.property.md)
  The location of the window’s backing store.
- [var preferredBackingLocation: NSWindow.BackingLocation](./preferredbackinglocation.md)
  A Boolean value that indicates the preferred location for the window’s backing store.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/showstoolbarbutton)*