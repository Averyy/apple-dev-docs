# boundsDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.

**Availability**:
- macOS

## Declaration

```swift
class let boundsDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSViewBoundsDidChangeNotification;
```

## Discussion

This notification posts only when the view’s [`postsBoundsChangedNotifications`](./postsboundschangednotifications.md) property is [`true`](../../Swift/true.md).

The notification object is the `NSView` object whose bounds rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [`bounds`](./bounds.md)
- [`setBoundsOrigin(_:)`](./setboundsorigin%28_%29.md)
- [`boundsRotation`](./boundsrotation.md)
- [`setBoundsSize(_:)`](./setboundssize%28_%29.md)
- [`translateOrigin(to:)`](./translateorigin%28to%29.md)
- [`scaleUnitSquare(to:)`](./scaleunitsquare%28to%29.md)
- [`rotate(byDegrees:)`](./rotate%28bydegrees%29.md)

Note that the bounds rectangle resizes automatically to track the frame rectangle. However, changes to the frame rectangle do not result in this bounds-changed notification.

To observe this notification using Swift concurrency, use [`NSView.BoundsDidChangeMessage`](./boundsdidchangemessage.md).

## See Also

### Modifying the bounds rectangle
- [var bounds: NSRect](./bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](./setboundsorigin%28_%29.md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](./setboundssize%28_%29.md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](./boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [NSView.BoundsDidChangeMessage](./boundsdidchangemessage.md)
- [var postsBoundsChangedNotifications: Bool](./postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/boundsdidchangenotification)*