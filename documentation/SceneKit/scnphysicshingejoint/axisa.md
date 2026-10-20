# axisA

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The axis that the hinge pivots around, relative to the node containing the first body.

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
var axisA: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 axisA;
```

## See Also

### Managing the Characteristics of a Hinge Joint
- [var bodyA: SCNPhysicsBody](./bodya.md)
  The first physics body connected by the joint.
- [var anchorA: SCNVector3](./anchora.md)
  The point at which the hinge connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](./bodyb.md)
  The second physics body connected by the joint.
- [var axisB: SCNVector3](./axisb.md)
  The axis that the hinge pivots around, relative to the node containing the second body.
- [var anchorB: SCNVector3](./anchorb.md)
  The point at which the hinge connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/axisa)*