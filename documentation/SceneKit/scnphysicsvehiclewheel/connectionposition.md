# connectionPosition

**Framework**: SceneKit  
**Kind**: property

The position of the wheel’s connection to the vehicle’s chassis.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var connectionPosition: SCNVector3 { get set }
```

#### Discussion

This vector is expressed in the coordinate space of the node containing the vehicle’s chassis. When you create a wheel from a node, SceneKit uses the node’s [`position`](scnnode/position.md) property as the wheel’s connection point.

## See Also

- [var axle: SCNVector3](scnphysicsvehiclewheel/axle.md)
  The direction of the axis that the wheel spins around to move the vehicle.
- [var steeringAxis: SCNVector3](scnphysicsvehiclewheel/steeringaxis.md)
  The direction of the axis that the wheel pivots around to steer the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/connectionposition)*