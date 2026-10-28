# speed

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The rate at which the simulation executes.

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
var speed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat speed;
```

## Discussion

The default value is `1.0`, which means that the simulation runs at normal speed. A value other than the default changes the rate at which time passes in the physics simulation. For example, a speed value of `2.0` indicates that time in the physics simulation passes twice as fast as the scene’s simulation time. A value of `0.0` pauses the physics simulation.

> **Note**:  Increasing the speed of the physics simulation reduces its accuracy.

## See Also

### Managing the Physics Simulation
- [var gravity: SCNVector3](./gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var timeStep: TimeInterval](./timestep.md)
  The time interval between updates to the physics simulation.
- [func updateCollisionPairs()](./updatecollisionpairs%28%29.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/speed)*