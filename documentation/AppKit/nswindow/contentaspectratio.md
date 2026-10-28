# contentAspectRatio

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s content aspect ratio.

**Availability**:
- macOS

## Declaration

```swift
var contentAspectRatio: NSSize { get set }
```

```objc
@property NSSize contentAspectRatio;
```

## Discussion

By default, the content aspect ratio (that is, height in relation to width) is `(0, 0)`. If you set the aspect ratio of a window’s content view, the dimensions of its content rectangle are constrained to integral multiples of that ratio when users resize it. You can set a window’s content view to any size programmatically, regardless of its aspect ratio. The value of this property takes precedence over [`aspectRatio`](./aspectratio.md).

## See Also

### Sizing Content
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
- [var maxFullScreenContentSize: NSSize](./maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](./minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentaspectratio)*