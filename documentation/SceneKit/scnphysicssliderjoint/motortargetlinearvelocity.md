# motorTargetLinearVelocity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The velocity at which the joint’s connected bodies should slide.

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
var motorTargetLinearVelocity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat motorTargetLinearVelocity;
```

#### Discussion

At the default value of `0.0`, the joint moves only when an external force acts on one of its connected bodies. Changing this value causes the joint to act as a linear motor, continuously applying a force (specified by the [`motorMaximumForce`](./motormaximumforce.md) property) until its connected bodies are moving along the sliding axis of the joint at the new velocity.

## See Also

### Applying Forces and Torques
- [var motorMaximumForce: CGFloat](./motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorTargetAngularVelocity: CGFloat](./motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.
- [var motorMaximumTorque: CGFloat](./motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motortargetlinearvelocity)*