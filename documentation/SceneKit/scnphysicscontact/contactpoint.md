# contactPoint

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The contact point between the two physics bodies, in scene coordinates.

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
var contactPoint: SCNVector3 { get }
```

```objc
@property (nonatomic, readonly) SCNVector3 contactPoint;
```

## See Also

### Inspecting the Contact Properties
- [var nodeA: SCNNode](./nodea.md)
  The node containing the first body in the contact.
- [var nodeB: SCNNode](./nodeb.md)
  The node containing the second body in the contact.
- [var contactNormal: SCNVector3](./contactnormal.md)
  The normal vector at the contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](./collisionimpulse.md)
  The force over time of the collision, in newton-seconds.
- [var penetrationDistance: CGFloat](./penetrationdistance.md)
  The distance of overlap, in units of scene coordinate space, between the two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscontact/contactpoint)*