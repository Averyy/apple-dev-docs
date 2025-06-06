# applyLinearImpulse(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Applies an impulse to the physics body at its center of mass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func applyLinearImpulse(_ impulse: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `impulse`: An impulse in newton seconds.
- `referenceEntity`: The reference entity that defines the coordinate   space in which   is defined.

## See Also

- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/applylinearimpulse(_:relativeto:))*