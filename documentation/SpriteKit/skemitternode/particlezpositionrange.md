# particleZPositionRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s depth.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var particleZPositionRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the z position of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particlePosition: CGPoint](skemitternode/particleposition.md)
  The average starting position for a particle.
- [var particlePositionRange: CGVector](skemitternode/particlepositionrange.md)
  The range of allowed random values for a particle’s position.
- [var particleZPosition: CGFloat](skemitternode/particlezposition.md)
  The average starting depth of a particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlezpositionrange)*