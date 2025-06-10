# addBehavior(_:)

**Framework**: SceneKit  
**Kind**: method

Adds a behavior to the physics world.

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
func addBehavior(_ behavior: SCNPhysicsBehavior)
```

#### Discussion

Physics behaviors constrain or modify the effects of the physics simulation on sets of physics bodies. For example, the [`SCNPhysicsHingeJoint`](scnphysicshingejoint.md) behavior causes two bodies to move as if connected by a hinge that pivots around a specific axis, and the [`SCNPhysicsVehicle`](scnphysicsvehicle.md) behavior causes a body to roll like a car or other wheeled vehicle.

To use a behavior in your scene, follow these steps:

1. Create [`SCNPhysicsBody`](scnphysicsbody.md) objects and attach them to each node that participates in the behavior.
2. Create and configure a behavior object joining the physics bodies. See [`SCNPhysicsBehavior`](scnphysicsbehavior.md) for a list of behavior classes.
3. Call [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) on your scene’s physics world object to add the behavior to the physics simulation.

## Parameters

- `behavior`: The behavior to be added.

## See Also

- [func removeBehavior(SCNPhysicsBehavior)](scnphysicsworld/removebehavior(_:).md)
  Removes a behavior from the physics world.
- [var allBehaviors: [SCNPhysicsBehavior]](scnphysicsworld/allbehaviors.md)
  The list of behaviors affecting bodies in the physics world.
- [func removeAllBehaviors()](scnphysicsworld/removeallbehaviors.md)
  Removes all behaviors affecting bodies in the physics world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/addbehavior(_:))*