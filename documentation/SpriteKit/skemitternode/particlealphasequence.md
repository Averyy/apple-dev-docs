# particleAlphaSequence

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The sequence used to specify the alpha value of a particle over its lifetime.

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
var particleAlphaSequence: SKKeyframeSequence? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKKeyframeSequence * particleAlphaSequence;
```

## Mentions

- [Animating Particle Properties Across Disparate Values](../animating-particle-properties-across-disparate-values.md)
- [Using Keyframe Sequence to effect Custom Interpolation](../using-keyframe-sequence-to-effect-custom-interpolation.md)

## Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleAlpha`](./particlealpha.md), [`particleAlphaRange`](./particlealpharange.md), and [`particleAlphaSpeed`](./particlealphaspeed.md) properties are ignored. Instead, the sequence is used to specify the alpha value.

## See Also

### Blending Particles with the Framebuffer
- [var particleBlendMode: SKBlendMode](./particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlpha: CGFloat](./particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaRange: CGFloat](./particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](./particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealphasequence)*