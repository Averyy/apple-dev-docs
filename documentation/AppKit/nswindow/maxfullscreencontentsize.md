# maxFullScreenContentSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A maximum size that is used to determine if a window can fit when it is in full screen in a tile.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var maxFullScreenContentSize: NSSize { get set }
```

```objc
@property NSSize maxFullScreenContentSize;
```

#### Discussion

By default, the system uses Auto Layout to determine the maximum size, so applications that don’t change window content upon entering full screen should not need to set the value of [`maxFullScreenContentSize`](./maxfullscreencontentsize.md). (If Auto Layout is not used, the system queries [`contentMinSize`](./contentminsize.md) and [`contentMaxSize`](./contentmaxsize.md).) If an application does significant rework of the user interface in full screen, then it may be necessary to set the value of [`maxFullScreenContentSize`](./maxfullscreencontentsize.md). You can use this property even if the window does not support full screen, but can be implicitly opted into supporting a full screen tile based on resizing behavior and window properties (for more information, see the [`collectionBehavior`](./collectionbehavior-swift.property.md) property).

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
- [var contentLayoutGuide: Any?](./contentlayoutguide.md)
  A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](./contentlayoutrect.md).
- [var contentLayoutRect: NSRect](./contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var minFullScreenContentSize: NSSize](./minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/maxfullscreencontentsize)*