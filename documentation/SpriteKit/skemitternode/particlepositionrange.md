# particlePositionRange

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The range of allowed random values for a particle’s position.

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
var particlePositionRange: CGVector { get set }
```

```objc
@property (nonatomic) CGVector particlePositionRange;
```

#### Discussion

The default value is `(0.0,0.0)`. If a component is non-zero, the same component of a particle’s position is randomly determined and may vary by plus or minus half of the range value.

## See Also

### Controlling Particle Position
- [var particlePosition: CGPoint](./particleposition.md)
  The average starting position for a particle.
- [var particleZPosition: CGFloat](./particlezposition.md)
  The average starting depth of a particle.
- [var particleZPositionRange: CGFloat](./particlezpositionrange.md)
  The range of allowed random values for a particle’s depth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlepositionrange)*