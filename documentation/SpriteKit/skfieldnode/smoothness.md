# smoothness

**Framework**: SpriteKit  
**Kind**: property

The smoothness of the noise used to generate the forces.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
var smoothness: Float { get set }
```

#### Discussion

This parameter should be a value between `0.0` and `1.0`, where `1.0` represents a uniform smoothness.

## See Also

- [var animationSpeed: Float](skfieldnode/animationspeed.md)
  The rate at which a noise or turbulence field node changes.
- [var direction: vector_float3](skfieldnode/direction.md)
  The direction of a velocity field node.
- [var texture: SKTexture?](skfieldnode/texture.md)
  A normal texture that specifies the velocities at different points in a velocity field node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/smoothness)*