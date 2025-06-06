# contentLayoutGuide

**Framework**: AppKit  
**Kind**: property

A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](nswindow/contentlayoutrect.md).

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var contentLayoutGuide: Any? { get }
```

## See Also

- [var contentAspectRatio: NSSize](nswindow/contentaspectratio.md)
  The window’s content aspect ratio.
- [var contentMinSize: NSSize](nswindow/contentminsize.md)
  The minimum size of the window’s content view in the window’s base coordinate system.
- [func setContentSize(NSSize)](nswindow/setcontentsize(_:).md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
- [var contentMaxSize: NSSize](nswindow/contentmaxsize.md)
  The maximum size of the window’s content view in the window’s base coordinate system.
- [var contentResizeIncrements: NSSize](nswindow/contentresizeincrements.md)
  The window’s content-view resizing increments.
- [var contentLayoutRect: NSRect](nswindow/contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var maxFullScreenContentSize: NSSize](nswindow/maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](nswindow/minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentlayoutguide)*