# particleColorBlendFactorSpeed

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The rate at which the color blend factor changes per second.

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
var particleColorBlendFactorSpeed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleColorBlendFactorSpeed;
```

#### Discussion

The default value is `0.0`.

## See Also

### Controlling How the Texture is Blended with Particle Color
- [var particleColorBlendFactorSequence: SKKeyframeSequence?](./particlecolorblendfactorsequence.md)
  The sequence used to specify the color blend factor of a particle over its lifetime.
- [var particleColorBlendFactor: CGFloat](./particlecolorblendfactor.md)
  The average starting value for the color blend factor.
- [var particleColorBlendFactorRange: CGFloat](./particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactorspeed)*