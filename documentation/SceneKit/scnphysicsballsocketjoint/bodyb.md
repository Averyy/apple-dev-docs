# bodyB

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The second physics body connected by the joint.

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
var bodyB: SCNPhysicsBody? { get }
```

```objc
@property (nonatomic, readonly, nullable) SCNPhysicsBody * bodyB;
```

## Discussion

This property’s value is `nil` if the joint was created using the [`init(body:anchor:)`](./init%28body,anchor%29.md) method.

## See Also

### Managing the Characteristics of a Ball and Socket Joint
- [var bodyA: SCNPhysicsBody](./bodya.md)
  The first physics body connected by the joint.
- [var anchorA: SCNVector3](./anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var anchorB: SCNVector3](./anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/bodyb)*