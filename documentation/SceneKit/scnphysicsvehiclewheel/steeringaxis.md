# steeringAxis

**Framework**: SceneKit  
**Kind**: property

The direction of the axis that the wheel pivots around to steer the vehicle.

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
var steeringAxis: SCNVector3 { get set }
```

#### Discussion

This vector is expressed in the coordinate space of the node containing the vehicle’s chassis. The default steering axis is `{0.0, -1.0, 0.0}`.

When you steer a wheel using the vehicle’s [`setSteeringAngle(_:forWheelAt:)`](scnphysicsvehicle/setsteeringangle(_:forwheelat:).md) method, the wheel pivots relative to this axis. For example, you can implement a vehicle whose rear wheels steer opposite its front wheels by reversing this vector’s direction for the rear wheels and then applying the same steering angle to all wheels.

## See Also

- [var connectionPosition: SCNVector3](scnphysicsvehiclewheel/connectionposition.md)
  The position of the wheel’s connection to the vehicle’s chassis.
- [var axle: SCNVector3](scnphysicsvehiclewheel/axle.md)
  The direction of the axis that the wheel spins around to move the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/steeringaxis)*