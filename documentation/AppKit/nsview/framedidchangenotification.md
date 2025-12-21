# frameDidChangeNotification

**Framework**: AppKit  
**Kind**: property

A notification that posts when the view’s frame rectangle changes to a new value.

**Availability**:
- macOS ?+

## Declaration

```swift
class let frameDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification posts only when the view’s [`postsFrameChangedNotifications`](nsview/postsframechangednotifications.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

The notification object is the `NSView` object whose frame rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [`frame`](nsview/frame.md)
- [`setFrameOrigin(_:)`](nsview/setframeorigin(_:).md)
- [`frameRotation`](nsview/framerotation.md)
- [`setFrameSize(_:)`](nsview/setframesize(_:).md)

## See Also

- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](nsview/setframeorigin(_:).md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var postsFrameChangedNotifications: Bool](nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framedidchangenotification)*