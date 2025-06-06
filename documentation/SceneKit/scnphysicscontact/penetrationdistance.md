# penetrationDistance

**Framework**: SceneKit  
**Kind**: property

The distance of overlap, in units of scene coordinate space, between the two physics bodies.

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
var penetrationDistance: CGFloat { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact/penetrationdistance)*