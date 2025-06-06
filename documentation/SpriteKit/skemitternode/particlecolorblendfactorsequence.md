# particleColorBlendFactorSequence

**Framework**: SpriteKit  
**Kind**: property

The sequence used to specify the color blend factor of a particle over its lifetime.

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
@MainActor
var particleColorBlendFactorSequence: SKKeyframeSequence? { get set }
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)
- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)

#### Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleColorBlendFactor`](skemitternode/particlecolorblendfactor.md), [`particleColorBlendFactorRange`](skemitternode/particlecolorblendfactorrange.md), and [`particleColorBlendFactorSpeed`](skemitternode/particlecolorblendfactorspeed.md) properties are ignored. Instead, the sequence is used to specify the color blend factor.

## See Also

- [var particleColorBlendFactor: CGFloat](skemitternode/particlecolorblendfactor.md)
  The average starting value for the color blend factor.
- [var particleColorBlendFactorRange: CGFloat](skemitternode/particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](skemitternode/particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactorsequence)*