# particleAlphaRange

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The range of allowed random values for a particle’s starting alpha value.

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
var particleAlphaRange: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleAlphaRange;
```

#### Discussion

The default value is `0.0`. If non-zero, the initial alpha value of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

### Blending Particles with the Framebuffer
- [var particleBlendMode: SKBlendMode](./particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](./particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](./particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaSpeed: CGFloat](./particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealpharange)*