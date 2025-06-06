# SCNPhysicsWorld

**Framework**: SceneKit  
**Kind**: class

The global simulation of collisions, gravity, joints, and other physics effects in a scene.

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
class SCNPhysicsWorld
```

#### Overview

You do not create [`SCNPhysicsWorld`](scnphysicsworld.md) objects directly; instead, read the [`physicsWorld`](scnscene/physicsworld.md) property of an [`SCNScene`](scnscene.md) object. Use physics world object to perform the following tasks:

- Manage global properties of the simulation, such as its speed and constant gravity. (For more precise control of gravity and similar effects, see the [`SCNPhysicsField`](scnphysicsfield.md) class.)
- Register behaviors that modify interactions between the scene’s physics bodies, such as joints and vehicles. For more details, see [`SCNPhysicsBehavior`](scnphysicsbehavior.md).
- Specify a delegate object to receive messages when two physics bodies contact each other
- Perform specific contact tests, and search for physics bodies in the scene using ray and sweep tests.

## Topics

### Managing the Physics Simulation
- [var gravity: SCNVector3](scnphysicsworld/gravity.md)
  A vector that specifies the gravitational acceleration applied to physics bodies in the physics world.
- [var speed: CGFloat](scnphysicsworld/speed.md)
  The rate at which the simulation executes.
- [var timeStep: TimeInterval](scnphysicsworld/timestep.md)
  The time interval between updates to the physics simulation.
- [func updateCollisionPairs()](scnphysicsworld/updatecollisionpairs.md)
  Forces the physics engine to reevaluate possible collisions between physics bodies.
### Registering Physics Behaviors
- [func addBehavior(SCNPhysicsBehavior)](scnphysicsworld/addbehavior(_:).md)
  Adds a behavior to the physics world.
- [func removeBehavior(SCNPhysicsBehavior)](scnphysicsworld/removebehavior(_:).md)
  Removes a behavior from the physics world.
- [var allBehaviors: [SCNPhysicsBehavior]](scnphysicsworld/allbehaviors.md)
  The list of behaviors affecting bodies in the physics world.
- [func removeAllBehaviors()](scnphysicsworld/removeallbehaviors.md)
  Removes all behaviors affecting bodies in the physics world.
### Detecting Contacts Between Physics Bodies
- [var contactDelegate: (any SCNPhysicsContactDelegate)?](scnphysicsworld/contactdelegate.md)
  A delegate that is called when two physics bodies come in contact with each other.
- [func contactTestBetween(SCNPhysicsBody, SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttestbetween(_:_:options:).md)
  Checks for contacts between two physics bodies.
- [func contactTest(with: SCNPhysicsBody, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/contacttest(with:options:).md)
  Checks for contacts between one physics body and any other bodies in the physics world.
### Searching for Physics Bodies
- [func rayTestWithSegment(from: SCNVector3, to: SCNVector3, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNHitTestResult]](scnphysicsworld/raytestwithsegment(from:to:options:).md)
  Searches for physics bodies along a line segment between two points in the physics world.
- [func convexSweepTest(with: SCNPhysicsShape, from: SCNMatrix4, to: SCNMatrix4, options: [SCNPhysicsWorld.TestOption : Any]?) -> [SCNPhysicsContact]](scnphysicsworld/convexsweeptest(with:from:to:options:).md)
  Searches for physics bodies in the space formed by moving a convex shape through the physics world.
### Search Options
- [SCNPhysicsWorld.TestOption](scnphysicsworld/testoption.md)
  Keys in options dictionaries that affect how SceneKit searches for bodies in a collision, ray, or sweep test.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsField](scnphysicsfield.md)
  An object that applies forces, such as gravitation, electromagnetism, and turbulence, to physics bodies within a certain area of effect.
- [class SCNPhysicsBehavior](scnphysicsbehavior.md)
  The abstract superclass for joints, vehicle simulations, and other high-level behaviors that incorporate multiple physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld)*