# setLimits(_:)

**Framework**: Dockkit  
**Kind**: method

Sets limits for the axes of rotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func setLimits(_ limits: DockAccessory.Limits) throws
```

#### Discussion

Limits only apply to the current tracking session. Afterwards, the orientation specifications default to the manufacturer limits. This method impacts primarily subsequent calls to [`setOrientation(_:duration:relative:)`](dockaccessory/setorientation(_:duration:relative:)-2epe2.md) and [`setOrientation(_:duration:relative:)`](dockaccessory/setorientation(_:duration:relative:)-6b0fl.md). Limits only apply to the current tracking session. When the session ends, the orientation specifications default to the manufacturer limits.

This method only works when you disable system tracking.

> **Note**: An error if all parameters are `nil`, or if the dock accessory doesn’t support the given axis.

## Parameters

- `limits`: The upper and lower limit of orientation, in radians, for each of the supported axes.

## See Also

- [func setOrientation(Vector3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-2epe2.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setOrientation(Rotation3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-6b0fl.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setAngularVelocity(Vector3D) async throws](dockaccessory/setangularvelocity(_:).md)
  Sets the angular velocity of each axis of orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setlimits(_:))*