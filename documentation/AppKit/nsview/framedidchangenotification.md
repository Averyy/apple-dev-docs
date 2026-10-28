# frameDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the view’s frame rectangle changes to a new value.

**Availability**:
- macOS

## Declaration

```swift
class let frameDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSViewFrameDidChangeNotification;
```

## Discussion

This notification posts only when the view’s [`postsFrameChangedNotifications`](./postsframechangednotifications.md) property is [`true`](../../Swift/true.md).

The notification object is the `NSView` object whose frame rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [`frame`](./frame.md)
- [`setFrameOrigin(_:)`](./setframeorigin%28_%29.md)
- [`frameRotation`](./framerotation.md)
- [`setFrameSize(_:)`](./setframesize%28_%29.md)

To observe this notification using Swift concurrency, use [`NSView.FrameDidChangeMessage`](./framedidchangemessage.md).

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
- [NSView.FrameDidChangeMessage](./framedidchangemessage.md)
- [var postsFrameChangedNotifications: Bool](./postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framedidchangenotification)*