# bounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view’s bounds rectangle, which expresses its location and size in its own coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var bounds: NSRect { get set }
```

```objc
@property NSRect bounds;
```

#### Discussion

By default, this property contains a rectangle whose origin is (0, 0) and whose size matches the size of the view’s frame rectangle (measured in points). In macOS 10.5 and later, if the view is being rendered into an OpenGL graphics context (using an [`NSOpenGLContext`](../nsopenglcontext.md) object), the default bounds origin is still (0, 0) but the default bounds size is measured in pixels instead of points. Thus, for user space scale factors other than 1.0, the default size of the bounds rectangle may be bigger or smaller than the default size of the frame rectangle when drawing with OpenGL.

> ❗ **Important**:  Developers of OpenGL applications should not rely on the rectangle in this property to convert coordinates to pixels automatically in future releases. Instead, you should convert coordinates to device space explicitly using the [`convertPointToBase:`](./convertpointtobase_.md), [`convertSizeToBase:`](./convertsizetobase_.md), or [`convertRectToBase:`](./convertrecttobase_.md) methods or their earlier counterparts [`convert(_:to:)`](./convert%28_,to%29-6u9ir.md), [`convert(_:to:)`](./convert%28_,to%29-5nptx.md), or [`convert(_:to:)`](./convert%28_,to%29-3cqqt.md).

If you explicitly change the origin or size of the bounds rectangle, this property saves the rectangle you set. If you add a rotation factor to the view, however, that factor is also reflected in the returned bounds rectangle. You can determine if a rotation factor is in effect by getting the value of the [`boundsRotation`](./boundsrotation.md) property.

Changing the bounds does not mark the view as needing to be displayed. Set the [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md) when you want the view to be redisplayed. After changing the bounds rectangle, the view creates an internal transform, a tool for manipulating coordinates, (or appends these changes to an existing internal transform) to convert from frame coordinates to bounds coordinates in your view. As long as the width-to-height ratio of the two coordinate systems remains the same, your content appears normal. If the ratios differ, your content may appear skewed. For more information, see [View Coordinates](../view-coordinates.md).

Changing the value of this property results in the posting of an [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## See Also

### Related Documentation
- [var frame: NSRect](./frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
### Modifying the bounds rectangle
- [func setBoundsOrigin(NSPoint)](./setboundsorigin%28_%29.md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](./setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](./boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [NSView.BoundsDidChangeMessage](./boundsdidchangemessage.md)
- [var postsBoundsChangedNotifications: Bool](./postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/bounds)*