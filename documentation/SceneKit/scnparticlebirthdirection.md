# SCNParticleBirthDirection

**Framework**: SceneKit  
**Kind**: enum

Options for the initial direction of each emitted particle, used by the [`birthDirection`](scnparticlesystem/birthdirection.md) property.

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
enum SCNParticleBirthDirection
```

## Topics

### Constants
- [SCNParticleBirthDirection.constant](scnparticlebirthdirection/constant.md)
  The emitting direction is the same for all particles.
- [SCNParticleBirthDirection.surfaceNormal](scnparticlebirthdirection/surfacenormal.md)
  The emitting direction for each particle is along the surface normal vector at the point where the particle is emitted.
- [SCNParticleBirthDirection.random](scnparticlebirthdirection/random.md)
  SceneKit randomizes the emitting direction for each particle.
### Initializers
- [init?(rawValue: Int)](scnparticlebirthdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var emitterShape: SCNGeometry?](scnparticlesystem/emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [var birthLocation: SCNParticleBirthLocation](scnparticlesystem/birthlocation.md)
  The possible locations for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthLocation](scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](scnparticlesystem/birthlocation.md) property.
- [var birthDirection: SCNParticleBirthDirection](scnparticlesystem/birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [var emittingDirection: SCNVector3](scnparticlesystem/emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlebirthdirection)*