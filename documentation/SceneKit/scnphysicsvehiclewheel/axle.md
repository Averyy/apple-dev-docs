# axle

**Framework**: SceneKit  
**Kind**: property

The direction of the axis that the wheel spins around to move the vehicle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var axle: SCNVector3 { get set }
```

#### Discussion

This vector is expressed in the coordinate space of the node containing the vehicle’s chassis. The default axle direction is `{-1.0, 0.0, 0.0}`.

## See Also

- [var connectionPosition: SCNVector3](scnphysicsvehiclewheel/connectionposition.md)
  The position of the wheel’s connection to the vehicle’s chassis.
- [var steeringAxis: SCNVector3](scnphysicsvehiclewheel/steeringaxis.md)
  The direction of the axis that the wheel pivots around to steer the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/axle)*