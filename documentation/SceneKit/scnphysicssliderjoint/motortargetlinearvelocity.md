# motorTargetLinearVelocity

**Framework**: SceneKit  
**Kind**: property

The velocity at which the joint’s connected bodies should slide.

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
var motorTargetLinearVelocity: CGFloat { get set }
```

#### Discussion

At the default value of `0.0`, the joint moves only when an external force acts on one of its connected bodies. Changing this value causes the joint to act as a linear motor, continuously applying a force (specified by the [`motorMaximumForce`](scnphysicssliderjoint/motormaximumforce.md) property) until its connected bodies are moving along the sliding axis of the joint at the new velocity.

## See Also

- [var motorMaximumForce: CGFloat](scnphysicssliderjoint/motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorTargetAngularVelocity: CGFloat](scnphysicssliderjoint/motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.
- [var motorMaximumTorque: CGFloat](scnphysicssliderjoint/motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motortargetlinearvelocity)*