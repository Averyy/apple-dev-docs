# contentLayoutGuide

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](./contentlayoutrect.md).

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentLayoutGuide: Any? { get }
```

```objc
@property (readonly, nullable) id contentLayoutGuide;
```

## See Also

### Sizing Content
- [var contentAspectRatio: NSSize](./contentaspectratio.md)
  The window’s content aspect ratio.
- [var contentMinSize: NSSize](./contentminsize.md)
  The minimum size of the window’s content view in the window’s base coordinate system.
- [func setContentSize(NSSize)](./setcontentsize%28_%29.md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
- [var contentMaxSize: NSSize](./contentmaxsize.md)
  The maximum size of the window’s content view in the window’s base coordinate system.
- [var contentResizeIncrements: NSSize](./contentresizeincrements.md)
  The window’s content-view resizing increments.
- [var contentLayoutRect: NSRect](./contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var maxFullScreenContentSize: NSSize](./maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](./minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentlayoutguide)*