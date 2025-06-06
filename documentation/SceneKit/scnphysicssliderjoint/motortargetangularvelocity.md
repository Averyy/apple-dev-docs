# motorTargetAngularVelocity

**Framework**: SceneKit  
**Kind**: property

The angular velocity at which the joint’s connected bodies should rotate around it.

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
var motorTargetAngularVelocity: CGFloat { get set }
```

#### Discussion

At the default value of `0.0`, the joint moves only when an external force acts on one of its connected bodies. Changing this value causes the joint to act as a rotary motor, continuously applying a torque (specified by the [`motorMaximumTorque`](scnphysicssliderjoint/motormaximumtorque.md) property) until its connected bodies are rotating around the joint at the new angular velocity.

## See Also

- [var motorTargetLinearVelocity: CGFloat](scnphysicssliderjoint/motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorMaximumForce: CGFloat](scnphysicssliderjoint/motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorMaximumTorque: CGFloat](scnphysicssliderjoint/motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motortargetangularvelocity)*