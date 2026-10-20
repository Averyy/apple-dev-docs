# particleColorBlendFactorSequence

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The sequence used to specify the color blend factor of a particle over its lifetime.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var particleColorBlendFactorSequence: SKKeyframeSequence? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKKeyframeSequence * particleColorBlendFactorSequence;
```

## Mentions

- [Animating Particle Properties Across Disparate Values](../animating-particle-properties-across-disparate-values.md)
- [Using Keyframe Sequence to effect Custom Interpolation](../using-keyframe-sequence-to-effect-custom-interpolation.md)

#### Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleColorBlendFactor`](./particlecolorblendfactor.md), [`particleColorBlendFactorRange`](./particlecolorblendfactorrange.md), and [`particleColorBlendFactorSpeed`](./particlecolorblendfactorspeed.md) properties are ignored. Instead, the sequence is used to specify the color blend factor.

## See Also

### Controlling How the Texture is Blended with Particle Color
- [var particleColorBlendFactor: CGFloat](./particlecolorblendfactor.md)
  The average starting value for the color blend factor.
- [var particleColorBlendFactorRange: CGFloat](./particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](./particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactorsequence)*