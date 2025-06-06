# particleRotationRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s initial rotation, expressed as an angle in radians.

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
var particleRotationRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the initial rotation of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particleRotation: CGFloat](skemitternode/particlerotation.md)
  The average initial rotation of a particle, expressed as an angle in radians.
- [var particleRotationSpeed: CGFloat](skemitternode/particlerotationspeed.md)
  The speed at which a particle rotates, expressed in radians per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlerotationrange)*