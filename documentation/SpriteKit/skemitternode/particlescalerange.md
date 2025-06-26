# particleScaleRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s initial scale.

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
var particleScaleRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the initial scale of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particleScale: CGFloat](skemitternode/particlescale.md)
  The average initial scale factor of a particle.
- [var particleScaleSpeed: CGFloat](skemitternode/particlescalespeed.md)
  The rate at which a particle’s scale factor changes per second.
- [var particleScaleSequence: SKKeyframeSequence?](skemitternode/particlescalesequence.md)
  The sequence used to specify the scale factor of a particle over its lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlescalerange)*