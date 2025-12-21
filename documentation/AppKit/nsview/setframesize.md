# setFrameSize(_:)

**Framework**: AppKit  
**Kind**: method

Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrameSize(_ newSize: NSSize)
```

#### Discussion

Changing the frame does not mark the view as needing to be displayed. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the view to be redisplayed.

Changing the frame size results in the posting of an [`frameDidChangeNotification`](nsview/framedidchangenotification.md) to the default notification center if the view is configured to do so.

In macOS 10.4 and later, you can override this method to support content preservation during live resizing. In your overridden implementation, include some conditional code to be executed only during a live resize operation. Your code must invalidate any portions of your view that need to be redrawn.

## Parameters

- `newSize`: An   structure specifying the new height and width of the frame rectangle.

## See Also

- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](nsview/setframeorigin(_:).md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [var postsFrameChangedNotifications: Bool](nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setframesize(_:))*