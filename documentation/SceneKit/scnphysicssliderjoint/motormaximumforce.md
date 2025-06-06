# motorMaximumForce

**Framework**: SceneKit  
**Kind**: property

The maximum linear force that the joint can apply to its connected bodies, in newtons.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var motorMaximumForce: CGFloat { get set }
```

#### Discussion

When you change the value of the [`motorTargetLinearVelocity`](scnphysicssliderjoint/motortargetlinearvelocity.md) property, the joint continuously applies a force of no greater than this magnitude until the bodies are moving at the target velocity. The default value is `1.0`.

## See Also

- [var motorTargetLinearVelocity: CGFloat](scnphysicssliderjoint/motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorTargetAngularVelocity: CGFloat](scnphysicssliderjoint/motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.
- [var motorMaximumTorque: CGFloat](scnphysicssliderjoint/motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motormaximumforce)*