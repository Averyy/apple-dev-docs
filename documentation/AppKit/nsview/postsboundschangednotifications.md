# postsBoundsChangedNotifications

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.

**Availability**:
- macOS

## Declaration

```swift
var postsBoundsChangedNotifications: Bool { get set }
```

```objc
@property BOOL postsBoundsChangedNotifications;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md) and the view’s bounds rectangle changes to a new value, the view posts a [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center. The notification is not posted when you set the bounds rectangle to the value it already has. The default value of this property is [`true`](../../Swift/true.md).

If the value of this property is currently [`false`](../../Swift/false.md) and the bounds have changed, changing the value to [`true`](../../Swift/true.md) causes the view to post a [`boundsDidChangeNotification`](./boundsdidchangenotification.md) notification immediately. This happens even when there has been no net change in the view’s bounds rectangle.

The following methods and properties can trigger a frame change notification:

- [`bounds`](./bounds.md)
- [`setBoundsOrigin(_:)`](./setboundsorigin%28_%29.md)
- [`setBoundsSize(_:)`](./setboundssize%28_%29.md)
- [`boundsRotation`](./boundsrotation.md)
- [`translateOrigin(to:)`](./translateorigin%28to%29.md)
- [`scaleUnitSquare(to:)`](./scaleunitsquare%28to%29.md)
- [`rotate(byDegrees:)`](./rotate%28bydegrees%29.md)

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
- [class let boundsDidChangeNotification: NSNotification.Name](./boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.
- [NSView.BoundsDidChangeMessage](./boundsdidchangemessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/postsboundschangednotifications)*