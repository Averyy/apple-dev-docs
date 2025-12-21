# particlePositionRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s position.

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
var particlePositionRange: CGVector { get set }
```

#### Discussion

The default value is `(0.0,0.0)`. If a component is non-zero, the same component of a particle’s position is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particlePosition: CGPoint](skemitternode/particleposition.md)
  The average starting position for a particle.
- [var particleZPosition: CGFloat](skemitternode/particlezposition.md)
  The average starting depth of a particle.
- [var particleZPositionRange: CGFloat](skemitternode/particlezpositionrange.md)
  The range of allowed random values for a particle’s depth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlepositionrange)*