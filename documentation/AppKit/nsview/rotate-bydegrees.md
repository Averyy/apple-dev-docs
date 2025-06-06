# rotate(byDegrees:)

**Framework**: AppKit  
**Kind**: method

Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rotate(byDegrees angle: CGFloat)
```

#### Discussion

See the [`boundsRotation`](nsview/boundsrotation.md) method description for more information. This method neither redisplays the view nor marks it as needing display. You must do this yourself by calling the [`display()`](nsview/display().md) method or setting the [`needsDisplay`](nsview/needsdisplay.md) property.

This method posts an [`boundsDidChangeNotification`](nsview/boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `angle`: A   value specifying the angle of rotation, in degrees.

## See Also

- [var frameRotation: CGFloat](nsview/framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var postsBoundsChangedNotifications: Bool](nsview/postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.
- [func translateOrigin(to: NSPoint)](nsview/translateorigin(to:).md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func scaleUnitSquare(to: NSSize)](nsview/scaleunitsquare(to:).md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rotate(bydegrees:))*