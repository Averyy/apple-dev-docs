# setAngularVelocity(_:)

**Framework**: DockKit  
**Kind**: method

Sets the angular velocity of each axis of orientation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func setAngularVelocity(_ angularVelocity: Vector3D) async throws
```

## Mentions

- [Modify rotation and positioning programmatically](modify-rotation-and-positioning-behavior-programmatically.md)

#### Discussion

The angular velocity is expressed in radians per second for pitch, yaw, and roll. This method works only when you disable system tracking.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if the accessory disconnects, or other errors if communication with the accessory fails.

[`DockKitError.notConnected`](dockkiterror/notconnected.md) if the accessory disconnects, or other errors if communication with the accessory fails.

## Parameters

- `angularVelocity`: A Vector3D object of the angular velocity to set, in axis/angle notation, corresponsing to radians per second for pitch, yaw, and roll axes.

## See Also

- [func setLimits(DockAccessory.Limits) throws](dockaccessory/setlimits(_:).md)
  Sets limits for the axes of rotation.
- [func setOrientation(Vector3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-2epe2.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setOrientation(Rotation3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-6b0fl.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setangularvelocity(_:))*