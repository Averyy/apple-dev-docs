# collisionImpulse

**Framework**: SceneKit  
**Kind**: property

The force over time of the collision, in newton-seconds.

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
var collisionImpulse: CGFloat { get }
```

#### Discussion

This property’s value tells you how hard the bodies struck each other in a collision. For example, in a game you might allow a character to proceed unhindered after a minor collision, but take damage when struck with sufficient force.

## See Also

- [var nodeA: SCNNode](scnphysicscontact/nodea.md)
  The node containing the first body in the contact.
- [var nodeB: SCNNode](scnphysicscontact/nodeb.md)
  The node containing the second body in the contact.
- [var contactPoint: SCNVector3](scnphysicscontact/contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var contactNormal: SCNVector3](scnphysicscontact/contactnormal.md)
  The normal vector at the contact point between the two physics bodies, in scene coordinates.
- [var penetrationDistance: CGFloat](scnphysicscontact/penetrationdistance.md)
  The distance of overlap, in units of scene coordinate space, between the two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact/collisionimpulse)*