# particleAlpha

**Framework**: SpriteKit  
**Kind**: property

The average starting alpha value for a particle.

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
var particleAlpha: CGFloat { get set }
```

#### Discussion

The particle alpha value is equivalent to the [`alpha`](sknode/alpha.md) property of the [`SKNode`](sknode.md) class. The alpha component of the color that results from the texture and color blending state is multiplied by a particle’s alpha value. The resulting particle color is then blended with the parent’s framebuffer. The default value is `1.0`.

## See Also

- [var particleBlendMode: SKBlendMode](skemitternode/particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](skemitternode/particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlphaRange: CGFloat](skemitternode/particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](skemitternode/particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealpha)*