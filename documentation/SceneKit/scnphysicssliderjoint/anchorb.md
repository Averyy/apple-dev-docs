# anchorB

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The point at which the joint connects, relative to the node containing the second body.

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
var anchorB: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 anchorB;
```

## See Also

### Managing the Characteristics of a Slider Joint
- [var bodyA: SCNPhysicsBody](./bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](./axisa.md)
  The axis along which the first body can slide, relative to the node containing it.
- [var anchorA: SCNVector3](./anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](./bodyb.md)
  The second physics body connected by the joint.
- [var axisB: SCNVector3](./axisb.md)
  The axis along which the second body can slide, relative to the node containing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/anchorb)*