# particleAlpha

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The average starting alpha value for a particle.

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
var particleAlpha: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleAlpha;
```

#### Discussion

The particle alpha value is equivalent to the [`alpha`](../sknode/alpha.md) property of the [`SKNode`](../sknode.md) class. The alpha component of the color that results from the texture and color blending state is multiplied by a particle’s alpha value. The resulting particle color is then blended with the parent’s framebuffer. The default value is `1.0`.

## See Also

### Blending Particles with the Framebuffer
- [var particleBlendMode: SKBlendMode](./particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](./particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlphaRange: CGFloat](./particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](./particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealpha)*