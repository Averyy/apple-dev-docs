# motorTargetAngularVelocity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The angular velocity at which the joint’s connected bodies should rotate around it.

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
var motorTargetAngularVelocity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat motorTargetAngularVelocity;
```

## Discussion

At the default value of `0.0`, the joint moves only when an external force acts on one of its connected bodies. Changing this value causes the joint to act as a rotary motor, continuously applying a torque (specified by the [`motorMaximumTorque`](./motormaximumtorque.md) property) until its connected bodies are rotating around the joint at the new angular velocity.

## See Also

### Applying Forces and Torques
- [var motorTargetLinearVelocity: CGFloat](./motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorMaximumForce: CGFloat](./motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorMaximumTorque: CGFloat](./motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motortargetangularvelocity)*