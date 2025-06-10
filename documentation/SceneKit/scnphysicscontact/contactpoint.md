# contactPoint

**Framework**: SceneKit  
**Kind**: property

The contact point between the two physics bodies, in scene coordinates.

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
var contactPoint: SCNVector3 { get }
```

## See Also

- [var nodeA: SCNNode](scnphysicscontact/nodea.md)
  The node containing the first body in the contact.
- [var nodeB: SCNNode](scnphysicscontact/nodeb.md)
  The node containing the second body in the contact.
- [var contactNormal: SCNVector3](scnphysicscontact/contactnormal.md)
  The normal vector at the contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](scnphysicscontact/collisionimpulse.md)
  The force over time of the collision, in newton-seconds.
- [var penetrationDistance: CGFloat](scnphysicscontact/penetrationdistance.md)
  The distance of overlap, in units of scene coordinate space, between the two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact/contactpoint)*