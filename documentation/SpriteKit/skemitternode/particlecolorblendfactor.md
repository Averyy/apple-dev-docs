# particleColorBlendFactor

**Framework**: SpriteKit  
**Kind**: property

The average starting value for the color blend factor.

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
var particleColorBlendFactor: CGFloat { get set }
```

#### Discussion

The default value is `0.0`, which means that the texture is used as is, ignoring the particle’s color. Otherwise, the texture is blended with the color. The maximum value is `1.0`, which means the particle renders with a full-tint color.

## See Also

- [var particleColorBlendFactorSequence: SKKeyframeSequence?](skemitternode/particlecolorblendfactorsequence.md)
  The sequence used to specify the color blend factor of a particle over its lifetime.
- [var particleColorBlendFactorRange: CGFloat](skemitternode/particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](skemitternode/particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorblendfactor)*