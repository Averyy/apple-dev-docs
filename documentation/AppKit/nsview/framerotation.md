# frameRotation

**Framework**: AppKit  
**Kind**: property

The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var frameRotation: CGFloat { get set }
```

#### Discussion

Positive values indicate counterclockwise rotation. Negative values indicate clockwise rotation. Rotation is performed around the origin of the frame rectangle. Changing the value of this property does not mark the view as needing to be displayed. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the view to be redisplayed.

Changing the frame rotation value results in the posting of an [`frameDidChangeNotification`](nsview/framedidchangenotification.md) to the default notification center if the view is configured to do so.

## See Also

- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](nsview/setframeorigin(_:).md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [var postsFrameChangedNotifications: Bool](nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framerotation)*