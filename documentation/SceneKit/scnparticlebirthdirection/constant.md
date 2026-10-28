# SCNParticleBirthDirection.constant

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The emitting direction is the same for all particles.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
case constant
```

```c
SCNParticleBirthDirectionConstant
```

## Discussion

When using this mode, the [`emittingDirection`](../scnparticlesystem/emittingdirection.md) property determines the base direction for all particles, and the [`spreadingAngle`](../scnparticlesystem/spreadingangle.md) property adds random variation to this direction.

## See Also

### Constants
- [SCNParticleBirthDirection.surfaceNormal](./surfacenormal.md)
  The emitting direction for each particle is along the surface normal vector at the point where the particle is emitted.
- [SCNParticleBirthDirection.random](./random.md)
  SceneKit randomizes the emitting direction for each particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection/constant)*