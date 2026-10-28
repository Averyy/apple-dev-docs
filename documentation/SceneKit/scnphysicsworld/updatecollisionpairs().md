# updateCollisionPairs()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Forces the physics engine to reevaluate possible collisions between physics bodies.

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
func updateCollisionPairs()
```

```objc
- (void) updateCollisionPairs;
```

## Discussion

By default, SceneKit checks for collisions between physics bodies only once per simulation step. If you directly change the positions of any physics bodies outside of a [`SCNPhysicsContactDelegate`](../scnphysicscontactdelegate.md) method, call the [`updateCollisionPairs()`](./updatecollisionpairs%28%29.md) method before using any of the methods listed in Searching for Physics Bodies Detecting Contacts Between Physics Bodies.

## See Also

### Related Documentation
- [var contactDelegate: (any SCNPhysicsContactDelegate)?](./contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
### Managing the Physics Simulation
- [var gravity: SCNVector3](./gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](./speed.md)
  The rate at which the simulation executes.
- [var timeStep: TimeInterval](./timestep.md)
  The time interval between updates to the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/updatecollisionpairs())*