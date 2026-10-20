# motorMaximumTorque

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The maximum torque that the joint can apply to its connected bodies, in newton-meters.

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
var motorMaximumTorque: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat motorMaximumTorque;
```

#### Discussion

When you change the value of the [`motorTargetAngularVelocity`](./motortargetangularvelocity.md) property, the joint continuously applies a force of no greater than this magnitude until the bodies are rotating around the joint at the target angular velocity. The default value is `1.0`.

## See Also

### Applying Forces and Torques
- [var motorTargetLinearVelocity: CGFloat](./motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorMaximumForce: CGFloat](./motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorTargetAngularVelocity: CGFloat](./motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motormaximumtorque)*