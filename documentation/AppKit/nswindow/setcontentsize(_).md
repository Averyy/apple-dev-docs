# setContentSize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.

**Availability**:
- macOS

## Declaration

```swift
func setContentSize(_ size: NSSize)
```

```objc
- (void) setContentSize:(NSSize) size;
```

## Discussion

This size in turn alters the size of the `NSWindow` object itself. Note that the window server limits window sizes to 10,000; if necessary, be sure to limit `aSize` relative to the frame rectangle.

## Parameters

- `size`: The new size of the window’s content view in the window’s base coordinate system.

## See Also

### Related Documentation
- [func setFrame(NSRect, display: Bool)](./setframe%28_,display%29.md)
  Sets the origin and size of the window’s frame rectangle according to a given frame rectangle, thereby setting its position and size onscreen.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./framerect%28forcontentrect,stylemask%29.md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](./contentrect%28forframerect,stylemask%29.md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
### Sizing Content
- [var contentAspectRatio: NSSize](./contentaspectratio.md)
  The window’s content aspect ratio.
- [var contentMinSize: NSSize](./contentminsize.md)
  The minimum size of the window’s content view in the window’s base coordinate system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setcontentsize(_:))*