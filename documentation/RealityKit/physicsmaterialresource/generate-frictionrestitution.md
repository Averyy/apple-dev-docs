# generate(friction:restitution:)

**Framework**: RealityKit  
**Kind**: method

Generates a new material with the given characteristics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generate(friction: Float = 0.8, restitution: Float = 0.8) -> PhysicsMaterialResource
```

#### Return Value

A physics material resource.

## Parameters

- `friction`: The coefficient of friction, in the range  .
- `restitution`: The coefficient of restitution, in the range  .   Use values at the high end of the range to indicate materials that   experience elastic collisions, meaning that objects bounce off each   other and kinetic energy is conserved after a collision. Use low values   to indicate materials that lose kinetic energy when they collide.

## See Also

- [static func generate(staticFriction: Float, dynamicFriction: Float, restitution: Float) -> PhysicsMaterialResource](physicsmaterialresource/generate(staticfriction:dynamicfriction:restitution:).md)
  Creates a new material with the specified static friction, dynamic friction, and restitution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmaterialresource/generate(friction:restitution:))*