# SCNParticleBirthLocation

**Framework**: SceneKit  
**Kind**: enum

Options for the initial location of each emitted particle, used by the [`birthLocation`](scnparticlesystem/birthlocation.md) property.

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
enum SCNParticleBirthLocation
```

#### Overview

The [`emitterShape`](scnparticlesystem/emittershape.md) property determines the shape of the space in which new particles can be emitted, and the [`birthLocation`](scnparticlesystem/birthlocation.md) property determines the locations of new particles relative to this shape.

To make a system’s particles emit from a single point, set the [`emitterShape`](scnparticlesystem/emittershape.md) property to `nil` (the default). In this case, SceneKit ignores the [`birthLocation`](scnparticlesystem/birthlocation.md) property.

## Topics

### Constants
- [SCNParticleBirthLocation.surface](scnparticlebirthlocation/surface.md)
  New particles can be created at any location on the surface of the emitter shape.
- [SCNParticleBirthLocation.volume](scnparticlebirthlocation/volume.md)
  New particles can be created at any location within the volume of the emitter shape.
- [SCNParticleBirthLocation.vertex](scnparticlebirthlocation/vertex.md)
  New particles can be created at only at the locations of the vertices in the emitter shape.
### Initializers
- [init?(rawValue: Int)](scnparticlebirthlocation/init(rawvalue:).md)

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
- [var birthDirection: SCNParticleBirthDirection](scnparticlesystem/birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthDirection](scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](scnparticlesystem/birthdirection.md) property.
- [var emittingDirection: SCNVector3](scnparticlesystem/emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation)*