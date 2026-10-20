# steeringAxis

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The direction of the axis that the wheel pivots around to steer the vehicle.

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
var steeringAxis: SCNVector3 { get set }
```

```objc
@property SCNVector3 steeringAxis;
```

#### Discussion

This vector is expressed in the coordinate space of the node containing the vehicle’s chassis. The default steering axis is `{0.0, -1.0, 0.0}`.

When you steer a wheel using the vehicle’s [`setSteeringAngle(_:forWheelAt:)`](../scnphysicsvehicle/setsteeringangle%28_,forwheelat%29.md) method, the wheel pivots relative to this axis. For example, you can implement a vehicle whose rear wheels steer opposite its front wheels by reversing this vector’s direction for the rear wheels and then applying the same steering angle to all wheels.

## See Also

### Managing a Wheel’s Connection to a Vehicle
- [var connectionPosition: SCNVector3](./connectionposition.md)
  The position of the wheel’s connection to the vehicle’s chassis.
- [var axle: SCNVector3](./axle.md)
  The direction of the axis that the wheel spins around to move the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/steeringaxis)*