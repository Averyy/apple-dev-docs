# particleScale

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The average initial scale factor of a particle.

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
var particleScale: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleScale;
```

## Discussion

The default value is `1.0`.

## See Also

### Scaling Particles by a Factor
- [var particleScaleRange: CGFloat](./particlescalerange.md)
  The range of allowed random values for a particle’s initial scale.
- [var particleScaleSpeed: CGFloat](./particlescalespeed.md)
  The rate at which a particle’s scale factor changes per second.
- [var particleScaleSequence: SKKeyframeSequence?](./particlescalesequence.md)
  The sequence used to specify the scale factor of a particle over its lifetime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlescale)*