# rotate(byDegrees:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Rotates the view’s bounds rectangle by a specified degree value around the origin of the coordinate system, (0.0, 0.0).

**Availability**:
- macOS

## Declaration

```swift
func rotate(byDegrees angle: CGFloat)
```

```objc
- (void) rotateByAngle:(CGFloat) angle;
```

#### Discussion

See the [`boundsRotation`](./boundsrotation.md) method description for more information. This method neither redisplays the view nor marks it as needing display. You must do this yourself by calling the [`display()`](./display%28%29.md) method or setting the [`needsDisplay`](./needsdisplay.md) property.

This method posts an [`boundsDidChangeNotification`](./boundsdidchangenotification.md) to the default notification center if the view is configured to do so.

## Parameters

- `angle`: A `float` value specifying the angle of rotation, in degrees.

## See Also

### Related Documentation
- [var frameRotation: CGFloat](./framerotation.md)
  The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [var postsBoundsChangedNotifications: Bool](./postsboundschangednotifications.md)
  A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.
### Modifying the Coordinate System
- [func translateOrigin(to: NSPoint)](./translateorigin%28to%29.md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func scaleUnitSquare(to: NSSize)](./scaleunitsquare%28to%29.md)
  Scales the view’s coordinate system so that the unit square scales to the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rotate(bydegrees:))*