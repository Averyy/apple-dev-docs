# motorMaximumTorque

**Framework**: SceneKit  
**Kind**: property

The maximum torque that the joint can apply to its connected bodies, in newton-meters.

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
var motorMaximumTorque: CGFloat { get set }
```

#### Discussion

When you change the value of the [`motorTargetAngularVelocity`](scnphysicssliderjoint/motortargetangularvelocity.md) property, the joint continuously applies a force of no greater than this magnitude until the bodies are rotating around the joint at the target angular velocity. The default value is `1.0`.

## See Also

- [var motorTargetLinearVelocity: CGFloat](scnphysicssliderjoint/motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorMaximumForce: CGFloat](scnphysicssliderjoint/motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorTargetAngularVelocity: CGFloat](scnphysicssliderjoint/motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motormaximumtorque)*