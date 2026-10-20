# frameRotation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var frameRotation: CGFloat { get set }
```

```objc
@property CGFloat frameRotation;
```

#### Discussion

Positive values indicate counterclockwise rotation. Negative values indicate clockwise rotation. Rotation is performed around the origin of the frame rectangle. Changing the value of this property does not mark the view as needing to be displayed. Set the [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md) when you want the view to be redisplayed.

Changing the frame rotation value results in the posting of an [`frameDidChangeNotification`](./framedidchangenotification.md) to the default notification center if the view is configured to do so.

## See Also

### Related Documentation
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
### Modifying the Frame Rectangle
- [var frame: NSRect](./frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameOrigin(NSPoint)](./setframeorigin%28_%29.md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](./setframesize%28_%29.md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](./framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [NSView.FrameDidChangeMessage](./framedidchangemessage.md)
- [var postsFrameChangedNotifications: Bool](./postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framerotation)*