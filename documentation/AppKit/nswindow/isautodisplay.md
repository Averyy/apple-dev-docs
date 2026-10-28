# isAutodisplay

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window automatically displays views that need to be displayed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use +[NSAnimationContext runAnimationGroup:completionHandler:] to temporarily prevent AppKit's automatic deferred display mechanism from drawing.

## Declaration

```swift
var isAutodisplay: Bool { get set }
```

```objc
@property (getter=isAutodisplay) BOOL autodisplay;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the window automatically displays views that need to be displayed; otherwise, [`false`](../../Swift/false.md). If `autodisplay` is [`false`](../../Swift/false.md), the window or its views must be explicitly displayed.

Automatic display typically occurs on each pass through the event loop.

## See Also

### Related Documentation
- [var needsDisplay: Bool](../nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
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
- [var graphicsContext: NSGraphicsContext?](./graphicscontext.md)
  The graphics context associated with the window for the current thread.
- [var windowRef: UnsafeMutableRawPointer](./windowref.md)
  The Carbon window reference associated with the window, creating one if necessary.
- [var showsToolbarButton: Bool](./showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isautodisplay)*