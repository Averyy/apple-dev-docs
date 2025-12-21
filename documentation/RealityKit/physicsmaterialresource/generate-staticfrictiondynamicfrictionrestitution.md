# generate(staticFriction:dynamicFriction:restitution:)

**Framework**: RealityKit  
**Kind**: method

Creates a new material with the specified static friction, dynamic friction, and restitution.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(staticFriction: Float, dynamicFriction: Float, restitution: Float) -> PhysicsMaterialResource
```

## Parameters

- `staticFriction`: The static (stationary) friction coefficient in the range [0, ∞).
- `dynamicFriction`: The dynamic (moving) friction coefficient in the range [0, ∞).
- `restitution`: The coefficient of restitution (bounciness) in the range [0, 1].

## See Also

- [static func generate(friction: Float, restitution: Float) -> PhysicsMaterialResource](physicsmaterialresource/generate(friction:restitution:).md)
  Generates a new material with the given characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmaterialresource/generate(staticfriction:dynamicfriction:restitution:))*