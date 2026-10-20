# connectionPosition

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The position of the wheel’s connection to the vehicle’s chassis.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var connectionPosition: SCNVector3 { get set }
```

```objc
@property SCNVector3 connectionPosition;
```

#### Discussion

This vector is expressed in the coordinate space of the node containing the vehicle’s chassis. When you create a wheel from a node, SceneKit uses the node’s [`position`](../scnnode/position.md) property as the wheel’s connection point.

## See Also

### Managing a Wheel’s Connection to a Vehicle
- [var axle: SCNVector3](./axle.md)
  The direction of the axis that the wheel spins around to move the vehicle.
- [var steeringAxis: SCNVector3](./steeringaxis.md)
  The direction of the axis that the wheel pivots around to steer the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/connectionposition)*