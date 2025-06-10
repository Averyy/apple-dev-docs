# SCNParticleBirthDirection.surfaceNormal

**Framework**: SceneKit  
**Kind**: case

The emitting direction for each particle is along the surface normal vector at the point where the particle is emitted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case surfaceNormal
```

#### Discussion

The particle system creates new particles at points in space defined by the [`emitterShape`](scnparticlesystem/emittershape.md) geometry. When a new particle is emitted, the geometry’s surface normal vector at the point nearest the particle determines the particle’s initial direction. (Note that the [`birthLocation`](scnparticlesystem/birthlocation.md) property defines where particles may be created relative to the [`emitterShape`](scnparticlesystem/emittershape.md) geometry.)

This value has no effect if the [`emitterShape`](scnparticlesystem/emittershape.md) property value is `nil`.

## See Also

- [SCNParticleBirthDirection.constant](scnparticlebirthdirection/constant.md)
  The emitting direction is the same for all particles.
- [SCNParticleBirthDirection.random](scnparticlebirthdirection/random.md)
  SceneKit randomizes the emitting direction for each particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection/surfacenormal)*