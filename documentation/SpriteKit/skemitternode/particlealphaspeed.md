# particleAlphaSpeed

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The rate at which the alpha value of a particle changes per second.

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
var particleAlphaSpeed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleAlphaSpeed;
```

## Discussion

The default value is `0.0`.

## See Also

### Blending Particles with the Framebuffer
- [var particleBlendMode: SKBlendMode](./particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](./particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](./particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaRange: CGFloat](./particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlealphaspeed)*