# boundsDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the `NSView`‘s bounds rectangle changes to a new value independently of the frame rectangle, but only when the view’s [`postsBoundsChangedNotifications`](nsview/postsboundschangednotifications.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

**Availability**:
- macOS ?+

## Declaration

```swift
class let boundsDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSView` object whose bounds rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [`bounds`](nsview/bounds.md)
- [`setBoundsOrigin(_:)`](nsview/setboundsorigin(_:).md)
- [`boundsRotation`](nsview/boundsrotation.md)
- [`setBoundsSize(_:)`](nsview/setboundssize(_:).md)
- [`translateOrigin(to:)`](nsview/translateorigin(to:).md)
- [`scaleUnitSquare(to:)`](nsview/scaleunitsquare(to:).md)
- [`rotate(byDegrees:)`](nsview/rotate(bydegrees:).md)

Note that the bounds rectangle resizes automatically to track the frame rectangle. However, changes to the frame rectangle do not result in this bounds-changed notification.

## See Also

- [var bounds: NSRect](nsview/bounds.md)
  The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func setBoundsSize(NSSize)](nsview/setboundssize(_:).md)
  Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [var boundsRotation: CGFloat](nsview/boundsrotation.md)
  The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [var postsBoundsChangedNotifications: Bool](nsview/postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/boundsdidchangenotification)*