# contentMinSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum size of the window’s content view in the window’s base coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var contentMinSize: NSSize { get set }
```

```objc
@property NSSize contentMinSize;
```

#### Discussion

The minimum size constraint is enforced for resizing by the user as well as for the [`setContentSize(_:)`](./setcontentsize%28_%29.md) method and the `setFrame...` methods other than [`setFrame(_:display:)`](./setframe%28_,display%29.md) and [`setFrame(_:display:animate:)`](./setframe%28_,display,animate%29.md). This method takes precedence over the [`minSize`](./minsize.md) property.

## See Also

### Sizing Content
- [var contentAspectRatio: NSSize](./contentaspectratio.md)
  The window’s content aspect ratio.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentminsize)*