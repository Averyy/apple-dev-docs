# postsBoundsChangedNotifications

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var postsBoundsChangedNotifications: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the view’s bounds rectangle changes to a new value, the view posts a [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center. The notification is not posted when you set the bounds rectangle to the value it already has. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

If the value of this property is currently [`false`](https://developer.apple.com/documentation/Swift/false) and the bounds have changed, changing the value to [`true`](https://developer.apple.com/documentation/Swift/true) causes the view to post a [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) notification immediately. This happens even when there has been no net change in the view’s bounds rectangle.

The following methods and properties can trigger a frame change notification:

- [`bounds`](nsview/bounds.md)
- [`setBoundsOrigin(_:)`](nsview/setboundsorigin(_:).md)
- [`setBoundsSize(_:)`](nsview/setboundssize(_:).md)
- [`boundsRotation`](nsview/boundsrotation.md)
- [`translateOrigin(to:)`](nsview/translateorigin(to:).md)
- [`scaleUnitSquare(to:)`](nsview/scaleunitsquare(to:).md)
- [`rotate(byDegrees:)`](nsview/rotate(bydegrees:).md)

## See Also

- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](nsview/setboundssize(_:).md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [class let boundsDidChangeNotification: NSNotification.Name](nsview/boundsdidchangenotification.md)
  A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/postsboundschangednotifications)*