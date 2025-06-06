# applyImpulse(_:at:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Applies an impulse to the physics body at the specified position.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func applyImpulse(_ impulse: SIMD3<Float>, at position: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `impulse`: An impulse in newton seconds.
- `position`: The position at which to apply the impulse.
- `referenceEntity`: The reference entity that defines the coordinate   space in which   and   are defined.

## See Also

- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applylinearimpulse(_:relativeto:).md)
  Applies an impulse to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/applyimpulse(_:at:relativeto:))*