# contentResizeIncrements

**Framework**: AppKit  
**Kind**: property

The window’s content-view resizing increments.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentResizeIncrements: NSSize { get set }
```

#### Discussion

The value of this property restricts the user’s ability to resize the window so the width and height of its content view change by multiples of width and height increments. As the user resizes the window, the size of its content view changes by integral multiples of `contentResizeIncrements.width` and `contentResizeIncrements.height`. However, you can set a window’s size to any width and height programmatically. This property takes precedence over [`resizeIncrements`](nswindow/resizeincrements.md).

## See Also

- [var contentAspectRatio: NSSize](nswindow/contentaspectratio.md)
  The window’s content aspect ratio.
- [var contentMinSize: NSSize](nswindow/contentminsize.md)
  The minimum size of the window’s content view in the window’s base coordinate system.
- [func setContentSize(NSSize)](nswindow/setcontentsize(_:).md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
- [var contentMaxSize: NSSize](nswindow/contentmaxsize.md)
  The maximum size of the window’s content view in the window’s base coordinate system.
- [var contentLayoutGuide: Any?](nswindow/contentlayoutguide.md)
  A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](nswindow/contentlayoutrect.md).
- [var contentLayoutRect: NSRect](nswindow/contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var maxFullScreenContentSize: NSSize](nswindow/maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](nswindow/minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentresizeincrements)*