# contentMinSize

**Framework**: AppKit  
**Kind**: property

The minimum size of the window’s content view in the window’s base coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var contentMinSize: NSSize { get set }
```

#### Discussion

The minimum size constraint is enforced for resizing by the user as well as for the [`setContentSize(_:)`](nswindow/setcontentsize(_:).md) method and the `setFrame...` methods other than [`setFrame(_:display:)`](nswindow/setframe(_:display:).md) and [`setFrame(_:display:animate:)`](nswindow/setframe(_:display:animate:).md). This method takes precedence over the [`minSize`](nswindow/minsize.md) property.

## See Also

- [var contentAspectRatio: NSSize](nswindow/contentaspectratio.md)
  The window’s content aspect ratio.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentminsize)*