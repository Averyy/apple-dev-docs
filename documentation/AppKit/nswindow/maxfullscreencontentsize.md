# maxFullScreenContentSize

**Framework**: AppKit  
**Kind**: property

A maximum size that is used to determine if a window can fit when it is in full screen in a tile.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var maxFullScreenContentSize: NSSize { get set }
```

#### Discussion

By default, the system uses Auto Layout to determine the maximum size, so applications that don’t change window content upon entering full screen should not need to set the value of [`maxFullScreenContentSize`](nswindow/maxfullscreencontentsize.md). (If Auto Layout is not used, the system queries [`contentMinSize`](nswindow/contentminsize.md) and [`contentMaxSize`](nswindow/contentmaxsize.md).) If an application does significant rework of the user interface in full screen, then it may be necessary to set the value of [`maxFullScreenContentSize`](nswindow/maxfullscreencontentsize.md). You can use this property even if the window does not support full screen, but can be implicitly opted into supporting a full screen tile based on resizing behavior and window properties (for more information, see the [`collectionBehavior`](nswindow/collectionbehavior-swift.property.md) property).

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
- [var contentLayoutGuide: Any?](nswindow/contentlayoutguide.md)
  A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](nswindow/contentlayoutrect.md).
- [var contentLayoutRect: NSRect](nswindow/contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var minFullScreenContentSize: NSSize](nswindow/minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/maxfullscreencontentsize)*