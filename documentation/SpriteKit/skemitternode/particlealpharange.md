# particleAlphaRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s starting alpha value.

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
var particleAlphaRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the initial alpha value of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particleBlendMode: SKBlendMode](skemitternode/particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](skemitternode/particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](skemitternode/particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaSpeed: CGFloat](skemitternode/particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealpharange)*