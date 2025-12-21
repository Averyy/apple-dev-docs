# particleScaleSequence

**Framework**: SpriteKit  
**Kind**: property

The sequence used to specify the scale factor of a particle over its lifetime.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var particleScaleSequence: SKKeyframeSequence? { get set }
```

## Mentions

- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)
- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)

#### Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleScale`](skemitternode/particlescale.md), [`particleScaleRange`](skemitternode/particlescalerange.md), and [`particleScaleSpeed`](skemitternode/particlescalespeed.md) properties are ignored. Instead, the sequence is used to specify the scale factor.

## See Also

- [var particleScale: CGFloat](skemitternode/particlescale.md)
  The average initial scale factor of a particle.
- [var particleScaleRange: CGFloat](skemitternode/particlescalerange.md)
  The range of allowed random values for a particle’s initial scale.
- [var particleScaleSpeed: CGFloat](skemitternode/particlescalespeed.md)
  The rate at which a particle’s scale factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlescalesequence)*