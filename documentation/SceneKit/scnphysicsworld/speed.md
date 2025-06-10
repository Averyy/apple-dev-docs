# speed

**Framework**: SceneKit  
**Kind**: property

The rate at which the simulation executes.

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
var speed: CGFloat { get set }
```

#### Discussion

The default value is `1.0`, which means that the simulation runs at normal speed. A value other than the default changes the rate at which time passes in the physics simulation. For example, a speed value of `2.0` indicates that time in the physics simulation passes twice as fast as the scene’s simulation time. A value of `0.0` pauses the physics simulation.

> **Note**:  Increasing the speed of the physics simulation reduces its accuracy.

## See Also

- [var gravity: SCNVector3](scnphysicsworld/gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var timeStep: TimeInterval](scnphysicsworld/timestep.md)
  The time interval between updates to the physics simulation.
- [func updateCollisionPairs()](scnphysicsworld/updatecollisionpairs.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/speed)*