# particleBlendMode

**Framework**: SpriteKit  
**Kind**: property

The blending mode used to blend particles into the framebuffer.

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
var particleBlendMode: SKBlendMode { get set }
```

#### Discussion

The default value is [`SKBlendMode.alpha`](skblendmode/alpha.md).

## See Also

- [var particleAlphaSequence: SKKeyframeSequence?](skemitternode/particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](skemitternode/particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaRange: CGFloat](skemitternode/particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](skemitternode/particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particleblendmode)*