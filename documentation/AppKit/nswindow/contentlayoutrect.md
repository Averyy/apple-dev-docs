# contentLayoutRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The area inside the window that is for non-obscured content, in window coordinates.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentLayoutRect: NSRect { get }
```

```objc
@property (readonly) NSRect contentLayoutRect;
```

#### Discussion

Typically, the area represented by this property is the same as the frame of the [`contentView`](./contentview.md). However, for windows with [`NSFullSizeContentViewWindowMask`](../nsfullsizecontentviewwindowmask.md) set, there needs to be a way to determine the portion that is not under the toolbar. The [`contentLayoutRect`](./contentlayoutrect.md) property contains the portion of the layout that is not obscured under the toolbar. This property is KVO compliant.

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
- [var maxFullScreenContentSize: NSSize](./maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](./minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentlayoutrect)*