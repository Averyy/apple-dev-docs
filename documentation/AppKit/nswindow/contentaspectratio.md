# contentAspectRatio

**Framework**: AppKit  
**Kind**: property

The window’s content aspect ratio.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentAspectRatio: NSSize { get set }
```

#### Discussion

By default, the content aspect ratio (that is, height in relation to width) is `(0, 0)`. If you set the aspect ratio of a window’s content view, the dimensions of its content rectangle are constrained to integral multiples of that ratio when users resize it. You can set a window’s content view to any size programmatically, regardless of its aspect ratio. The value of this property takes precedence over [`aspectRatio`](nswindow/aspectratio.md).

## See Also

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
- [var maxFullScreenContentSize: NSSize](nswindow/maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](nswindow/minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentaspectratio)*