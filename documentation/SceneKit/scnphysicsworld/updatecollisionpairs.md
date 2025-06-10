# updateCollisionPairs()

**Framework**: SceneKit  
**Kind**: method

Forces the physics engine to reevaluate possible collisions between physics bodies.

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
func updateCollisionPairs()
```

#### Discussion

By default, SceneKit checks for collisions between physics bodies only once per simulation step. If you directly change the positions of any physics bodies outside of a [`SCNPhysicsContactDelegate`](scnphysicscontactdelegate.md) method, call the [`updateCollisionPairs()`](scnphysicsworld/updatecollisionpairs().md) method before using any of the methods listed in Searching for Physics Bodies Detecting Contacts Between Physics Bodies.

## See Also

- [var contactDelegate: (any SCNPhysicsContactDelegate)?](scnphysicsworld/contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
- [var gravity: SCNVector3](scnphysicsworld/gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](scnphysicsworld/speed.md)
  The rate at which the simulation executes.
- [var timeStep: TimeInterval](scnphysicsworld/timestep.md)
  The time interval between updates to the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/updatecollisionpairs())*