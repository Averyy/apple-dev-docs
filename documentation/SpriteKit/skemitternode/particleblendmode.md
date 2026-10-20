# particleBlendMode

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The blending mode used to blend particles into the framebuffer.

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
var particleBlendMode: SKBlendMode { get set }
```

```objc
@property (nonatomic) SKBlendMode particleBlendMode;
```

#### Discussion

The default value is [`SKBlendMode.alpha`](../skblendmode/alpha.md).

## See Also

### Blending Particles with the Framebuffer
- [var particleAlphaSequence: SKKeyframeSequence?](./particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](./particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaRange: CGFloat](./particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](./particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particleblendmode)*