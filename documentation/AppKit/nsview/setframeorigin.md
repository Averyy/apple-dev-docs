# setFrameOrigin(_:)

**Framework**: AppKit  
**Kind**: method

Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrameOrigin(_ newOrigin: NSPoint)
```

#### Discussion

Changing the frame does not mark the view as needing to be displayed. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/swift/true) when you want the view to be redisplayed.

Changing the frame origin results in the posting of an [`frameDidChangeNotification`](nsview/framedidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `newOrigin`: The point that is the new origin of the view’s frame.

## See Also

- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](nsview/framedidchangenotification.md)
  Posted whenever the view’s frame rectangle changes to a new value, but only when the view’s [`postsFrameChangedNotifications`](nsview/postsframechangednotifications.md) property is [`true`](https://developer.apple.com/documentation/swift/true).
- [var postsFrameChangedNotifications: Bool](nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setframeorigin(_:))*