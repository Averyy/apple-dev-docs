# angularVelocities

**Framework**: DockKit  
**Kind**: property

The angular velocity of each axis of rotation in radians.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
let angularVelocities: Vector3D
```

#### Discussion

The X, Y, and Z values are in radians per second corresponding to pitch, yaw, and roll axes.

## See Also

- [let angularPositions: Vector3D](dockaccessory/motionstate/angularpositions.md)
  The angles of the axes, in radians.
- [let timestamp: TimeInterval](dockaccessory/motionstate/timestamp.md)
  The current time, in UNIX epoch.
- [let error: (any Error)?](dockaccessory/motionstate/error.md)
  The error, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstate/angularvelocities)*