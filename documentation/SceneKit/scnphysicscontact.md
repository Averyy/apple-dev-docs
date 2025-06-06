# SCNPhysicsContact

**Framework**: SceneKit  
**Kind**: class

Detailed information about a contact between two physics bodies in a scene’s physics simulation.

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
class SCNPhysicsContact
```

#### Overview

You don’t create  [`SCNPhysicsContact`](scnphysicscontact.md) instances directly; SceneKit automatically creates these objects whenever contacts occur.

To receive contact messages, assign your custom class implementing the [`SCNPhysicsContactDelegate`](scnphysicscontactdelegate.md) protocol to the [`contactDelegate`](scnphysicsworld/contactdelegate.md) property of your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) obejct. Next, for each physics body in your scene, set the [`categoryBitMask`](scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) properties to define which interactions should generate contact messages.

## Topics

### Inspecting the Contact Properties
- [var nodeA: SCNNode](scnphysicscontact/nodea.md)
  The node containing the first body in the contact.
- [var nodeB: SCNNode](scnphysicscontact/nodeb.md)
  The node containing the second body in the contact.
- [var contactPoint: SCNVector3](scnphysicscontact/contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var contactNormal: SCNVector3](scnphysicscontact/contactnormal.md)
  The normal vector at the contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](scnphysicscontact/collisionimpulse.md)
  The force over time of the collision, in newton-seconds.
- [var penetrationDistance: CGFloat](scnphysicscontact/penetrationdistance.md)
  The distance of overlap, in units of scene coordinate space, between the two physics bodies.
### Instance Properties
- [var sweepTestFraction: CGFloat](scnphysicscontact/sweeptestfraction.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol SCNPhysicsContactDelegate](scnphysicscontactdelegate.md)
  Methods you can implement to respond when a contact or collision occurs between two physics bodies in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact)*