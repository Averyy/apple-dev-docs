# motorMaximumForce

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The maximum linear force that the joint can apply to its connected bodies, in newtons.

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
var motorMaximumForce: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat motorMaximumForce;
```

## Discussion

When you change the value of the [`motorTargetLinearVelocity`](./motortargetlinearvelocity.md) property, the joint continuously applies a force of no greater than this magnitude until the bodies are moving at the target velocity. The default value is `1.0`.

## See Also

### Applying Forces and Torques
- [var motorTargetLinearVelocity: CGFloat](./motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorTargetAngularVelocity: CGFloat](./motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.
- [var motorMaximumTorque: CGFloat](./motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/motormaximumforce)*