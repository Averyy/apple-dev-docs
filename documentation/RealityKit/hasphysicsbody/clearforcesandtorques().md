# clearForcesAndTorques()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Clears all forces previously added to the physics body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func clearForcesAndTorques()
```

## See Also

### Adding and clearing forces
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](./addforce%28_,relativeto%29.md)
  Applies a force to the physics body at its center of mass.
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](./addforce%28_,at,relativeto%29.md)
  Applies a force to the physics body at the specified position.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](./addtorque%28_,relativeto%29.md)
  Applies a torque to the physics body at its center of mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/clearforcesandtorques())*