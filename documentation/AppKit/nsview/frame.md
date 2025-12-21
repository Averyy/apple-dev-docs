# frame

**Framework**: AppKit  
**Kind**: property

The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var frame: NSRect { get set }
```

## Mentions

- [Adopting the system text cursor in custom text views](adopting-the-system-text-cursor-in-custom-text-views.md)

#### Discussion

Changing the value of this property repositions and resizes the view within the coordinate system of its superview. Changing the frame does not mark the view as needing to be displayed. Set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the view to be redisplayed.

If your view does not use a custom bounds rectangle, this method also sets the view’s bounds to match the size of the new frame. You can specify a custom bounds rectangle by changing the [`bounds`](nsview/bounds.md) property or by calling the [`setBoundsOrigin(_:)`](nsview/setboundsorigin(_:).md) or [`setBoundsSize(_:)`](nsview/setboundssize(_:).md) method explicitly. Once set, the view creates an internal transform to convert from frame coordinates to bounds coordinates. As long as the width-to-height ratio of the two coordinate systems remains the same, your content appears normal. If the ratios differ, your content may appear skewed.

The frame rectangle may be rotated relative to its superview’s coordinate system. For more information, see the [`frameRotation`](nsview/framerotation.md) property.

Changing the value of this property results in the posting of an [`frameDidChangeNotification`](nsview/framedidchangenotification.md) to the default notification center if the view is configured to do so.

## See Also

- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setFrameOrigin(NSPoint)](nsview/setframeorigin(_:).md)
  Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [class let frameDidChangeNotification: NSNotification.Name](nsview/framedidchangenotification.md)
  A notification that posts when the view’s frame rectangle changes to a new value.
- [var postsFrameChangedNotifications: Bool](nsview/postsframechangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its frame rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/frame)*