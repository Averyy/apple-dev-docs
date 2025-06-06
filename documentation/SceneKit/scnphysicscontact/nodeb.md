# nodeB

**Framework**: SceneKit  
**Kind**: property

The node containing the second body in the contact.

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
var nodeB: SCNNode { get }
```

#### Discussion

Use the node’s [`physicsBody`](scnnode/physicsbody.md) property to examine physics characteristics of the node.

## See Also

- [var nodeA: SCNNode](scnphysicscontact/nodea.md)
  The node containing the first body in the contact.
- [var contactPoint: SCNVector3](scnphysicscontact/contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var contactNormal: SCNVector3](scnphysicscontact/contactnormal.md)
  The normal vector at the contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](scnphysicscontact/collisionimpulse.md)
  The force over time of the collision, in newton-seconds.
- [var penetrationDistance: CGFloat](scnphysicscontact/penetrationdistance.md)
  The distance of overlap, in units of scene coordinate space, between the two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact/nodeb)*