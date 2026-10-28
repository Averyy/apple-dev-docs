# angularVelocities

**Framework**: DockKit  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The X, Y, and Z values are in radians per second corresponding to pitch, yaw, and roll axes.

## See Also

### Getting properties
- [let angularPositions: Vector3D](./angularpositions.md)
  The angles of the axes, in radians.
- [let timestamp: TimeInterval](./timestamp.md)
  The current time, in UNIX epoch.
- [let error: (any Error)?](./error.md)
  The error, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/motionstate/angularvelocities)*