# DockAccessory.MotionState

**Framework**: DockKit  
**Kind**: struct

An event that indicates the state of a dock accessory’s current position and speed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct MotionState
```

#### Overview

This event indicates the dock accessory’s current velocity and position along each supported axis of rotation. For more information, see [`motionStates`](dockaccessory/motionstates-swift.property.md).

## Topics

### Getting properties
- [let angularPositions: Vector3D](dockaccessory/motionstate/angularpositions.md)
  The angles of the axes, in radians.
- [let angularVelocities: Vector3D](dockaccessory/motionstate/angularvelocities.md)
  The angular velocity of each axis of rotation in radians.
- [let timestamp: TimeInterval](dockaccessory/motionstate/timestamp.md)
  The current time, in UNIX epoch.
- [let error: (any Error)?](dockaccessory/motionstate/error.md)
  The error, if any.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var motionStates: DockAccessory.MotionStates](dockaccessory/motionstates-swift.property.md)
  Motion information from the dock accessory that includes current orientation and velocity of all axes.
- [var limits: DockAccessory.Limits](dockaccessory/limits-swift.property.md)
  Current limits for the axes of rotation and maximum angular velocity.
- [DockAccessory.MotionStates](dockaccessory/motionstates-swift.struct.md)
  An asynchronous sequence of orientation and velocity updates from the device.
- [DockAccessory.Limits](dockaccessory/limits-swift.struct.md)
  Soft limits on multiple axes of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstate)*