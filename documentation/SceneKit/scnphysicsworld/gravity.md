# gravity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.

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
var gravity: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 gravity;
```

## Discussion

The components of this vector are measured in meters per second per second. The default value is `(0.0,-9.8,0.0)`.

This property applies a constant acceleration to all physics bodies in the world, simulating the effect of gravity near the surface of the Earth. For more sophisticated gravity effects, including limited areas of effect and strength proportional to distance, use the [`SCNPhysicsField`](../scnphysicsfield.md) class. When using fields, you may want to set this property to the zero vector so that fields provide all gravity effects in the physics world.

## See Also

### Managing the Physics Simulation
- [var speed: CGFloat](./speed.md)
  The rate at which the simulation executes.
- [var timeStep: TimeInterval](./timestep.md)
  The time interval between updates to the physics simulation.
- [func updateCollisionPairs()](./updatecollisionpairs%28%29.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/gravity)*