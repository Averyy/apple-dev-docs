# SCNPhysicsConeTwistJoint

**Framework**: SceneKit  
**Kind**: class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class SCNPhysicsConeTwistJoint
```

## Topics

### Initializers
- [convenience init(body: SCNPhysicsBody, frame: SCNMatrix4)](scnphysicsconetwistjoint/init(body:frame:).md)
- [convenience init(bodyA: SCNPhysicsBody, frameA: SCNMatrix4, bodyB: SCNPhysicsBody, frameB: SCNMatrix4)](scnphysicsconetwistjoint/init(bodya:framea:bodyb:frameb:).md)
### Instance Properties
- [var bodyA: SCNPhysicsBody](scnphysicsconetwistjoint/bodya.md)
- [var bodyB: SCNPhysicsBody?](scnphysicsconetwistjoint/bodyb.md)
- [var frameA: SCNMatrix4](scnphysicsconetwistjoint/framea.md)
- [var frameB: SCNMatrix4](scnphysicsconetwistjoint/frameb.md)
- [var maximumAngularLimit1: CGFloat](scnphysicsconetwistjoint/maximumangularlimit1.md)
- [var maximumAngularLimit2: CGFloat](scnphysicsconetwistjoint/maximumangularlimit2.md)
- [var maximumTwistAngle: CGFloat](scnphysicsconetwistjoint/maximumtwistangle.md)

## Relationships

### Inherits From
- [SCNPhysicsBehavior](scnphysicsbehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsHingeJoint](scnphysicshingejoint.md)
  A physics behavior that connects two bodies and allows them to pivot around each other on a single axis.
- [class SCNPhysicsSliderJoint](scnphysicssliderjoint.md)
  A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.
- [class SCNPhysicsBallSocketJoint](scnphysicsballsocketjoint.md)
  A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsconetwistjoint)*