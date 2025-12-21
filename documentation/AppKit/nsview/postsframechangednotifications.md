# postsFrameChangedNotifications

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view posts notifications when its frame rectangle changes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var postsFrameChangedNotifications: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the view’s frame rectangle changes to a new value, the view posts a [`frameDidChangeNotification`](nsview/framedidchangenotification.md) to the default notification center. The notification is not posted when you set the frame rectangle to the value it already has. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

If the value of this property is currently [`false`](https://developer.apple.com/documentation/Swift/false) and and the frame has changed, changing the value to [`true`](https://developer.apple.com/documentation/Swift/true) causes the view to post a [`frameDidChangeNotification`](nsview/framedidchangenotification.md) notification immediately. This happens even when there has been no net change in the view’s frame rectangle.

The following methods and properties can trigger a frame change notification:

- [`frame`](nsview/frame.md)
- [`setFrameOrigin(_:)`](nsview/setframeorigin(_:).md)
- [`setFrameSize(_:)`](nsview/setframesize(_:).md)
- [`frameRotation`](nsview/framerotation.md)

## See Also

- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](nsview/setframeorigin(_:).md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/postsframechangednotifications)*