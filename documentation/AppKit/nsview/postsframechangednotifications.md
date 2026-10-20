# postsFrameChangedNotifications

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view posts notifications when its frame rectangle changes.

**Availability**:
- macOS

## Declaration

```swift
var postsFrameChangedNotifications: Bool { get set }
```

```objc
@property BOOL postsFrameChangedNotifications;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md) and the view’s frame rectangle changes to a new value, the view posts a [`frameDidChangeNotification`](./framedidchangenotification.md) to the default notification center. The notification is not posted when you set the frame rectangle to the value it already has. The default value of this property is [`true`](../../Swift/true.md).

If the value of this property is currently [`false`](../../Swift/false.md) and and the frame has changed, changing the value to [`true`](../../Swift/true.md) causes the view to post a [`frameDidChangeNotification`](./framedidchangenotification.md) notification immediately. This happens even when there has been no net change in the view’s frame rectangle.

The following methods and properties can trigger a frame change notification:

- [`frame`](./frame.md)
- [`setFrameOrigin(_:)`](./setframeorigin%28_%29.md)
- [`setFrameSize(_:)`](./setframesize%28_%29.md)
- [`frameRotation`](./framerotation.md)

## See Also

### Modifying the Frame Rectangle
- [var frame: NSRect](./frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](./setframeorigin%28_%29.md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](./setframesize%28_%29.md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](./framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](./framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [NSView.FrameDidChangeMessage](./framedidchangemessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/postsframechangednotifications)*