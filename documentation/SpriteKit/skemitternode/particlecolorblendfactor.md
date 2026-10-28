# particleColorBlendFactor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The average starting value for the color blend factor.

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
var particleColorBlendFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleColorBlendFactor;
```

## Discussion

The default value is `0.0`, which means that the texture is used as is, ignoring the particle’s color. Otherwise, the texture is blended with the color. The maximum value is `1.0`, which means the particle renders with a full-tint color.

## See Also

### Controlling How the Texture is Blended with Particle Color
- [var particleColorBlendFactorSequence: SKKeyframeSequence?](./particlecolorblendfactorsequence.md)
  The sequence used to specify the color blend factor of a particle over its lifetime.
- [var particleColorBlendFactorRange: CGFloat](./particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](./particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactor)*