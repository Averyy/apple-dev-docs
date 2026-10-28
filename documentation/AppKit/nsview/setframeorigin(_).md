# setFrameOrigin(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.

**Availability**:
- macOS

## Declaration

```swift
func setFrameOrigin(_ newOrigin: NSPoint)
```

```objc
- (void) setFrameOrigin:(NSPoint) newOrigin;
```

## Discussion

Changing the frame does not mark the view as needing to be displayed. Set the [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md) when you want the view to be redisplayed.

Changing the frame origin results in the posting of an [`frameDidChangeNotification`](./framedidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `newOrigin`: The point that is the new origin of the view’s frame.

## See Also

### Modifying the Frame Rectangle
- [var frame: NSRect](./frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func setFrameSize(NSSize)](./setframesize%28_%29.md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](./framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](./framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [NSView.FrameDidChangeMessage](./framedidchangemessage.md)
- [var postsFrameChangedNotifications: Bool](./postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setframeorigin(_:))*