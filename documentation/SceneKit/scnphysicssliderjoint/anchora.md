# anchorA

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The point at which the joint connects, relative to the node containing the first body.

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
var anchorA: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 anchorA;
```

## See Also

### Managing the Characteristics of a Slider Joint
- [var bodyA: SCNPhysicsBody](./bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](./axisa.md)
  The axis along which the first body can slide, relative to the node containing it.
- [var bodyB: SCNPhysicsBody?](./bodyb.md)
  The second physics body connected by the joint.
- [var axisB: SCNVector3](./axisb.md)
  The axis along which the second body can slide, relative to the node containing it.
- [var anchorB: SCNVector3](./anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/anchora)*