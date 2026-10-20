# particleColorBlendFactorRange

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The range of allowed random values for a particle’s starting color blend factor.

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
var particleColorBlendFactorRange: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleColorBlendFactorRange;
```

#### Discussion

The default value is `0.0`. If non-zero, the initial color blend factor of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

### Controlling How the Texture is Blended with Particle Color
- [var particleColorBlendFactorSequence: SKKeyframeSequence?](./particlecolorblendfactorsequence.md)
  The sequence used to specify the color blend factor of a particle over its lifetime.
- [var particleColorBlendFactor: CGFloat](./particlecolorblendfactor.md)
  The average starting value for the color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](./particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactorrange)*