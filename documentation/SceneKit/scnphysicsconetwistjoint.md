# SCNPhysicsConeTwistJoint

**Framework**: SceneKit  
**Kind**: class  
**Role**: Class

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
class SCNPhysicsConeTwistJoint
```

```objc
@interface SCNPhysicsConeTwistJoint : SCNPhysicsBehavior
```

## Topics

### Initializers
- [convenience init(body: SCNPhysicsBody, frame: SCNMatrix4)](./scnphysicsconetwistjoint/init%28body,frame%29.md)
- [convenience init(bodyA: SCNPhysicsBody, frameA: SCNMatrix4, bodyB: SCNPhysicsBody, frameB: SCNMatrix4)](./scnphysicsconetwistjoint/init%28bodya,framea,bodyb,frameb%29.md)
### Instance Properties
- [var bodyA: SCNPhysicsBody](./scnphysicsconetwistjoint/bodya.md)
- [var bodyB: SCNPhysicsBody?](./scnphysicsconetwistjoint/bodyb.md)
- [var frameA: SCNMatrix4](./scnphysicsconetwistjoint/framea.md)
- [var frameB: SCNMatrix4](./scnphysicsconetwistjoint/frameb.md)
- [var maximumAngularLimit1: CGFloat](./scnphysicsconetwistjoint/maximumangularlimit1.md)
- [var maximumAngularLimit2: CGFloat](./scnphysicsconetwistjoint/maximumangularlimit2.md)
- [var maximumTwistAngle: CGFloat](./scnphysicsconetwistjoint/maximumtwistangle.md)

## Relationships

### Inherits From
- [SCNPhysicsBehavior](./scnphysicsbehavior.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Joints
- [class SCNPhysicsHingeJoint](./scnphysicshingejoint.md)
  A physics behavior that connects two bodies and allows them to pivot around each other on a single axis.
- [class SCNPhysicsSliderJoint](./scnphysicssliderjoint.md)
  A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.
- [class SCNPhysicsBallSocketJoint](./scnphysicsballsocketjoint.md)
  A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsconetwistjoint)*