# birthLocation

**Framework**: SceneKit  
**Kind**: property

The possible locations for newly spawned particles, relative to the emitter shape.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var birthLocation: SCNParticleBirthLocation { get set }
```

#### Discussion

This property defines locations for spawning new particles relative to the geometry specified in the [`emitterShape`](scnparticlesystem/emittershape.md) property. This property has no effect if the [`emitterShape`](scnparticlesystem/emittershape.md) property value is `nil`.

For example, if the emitter shape is an [`SCNBox`](scnbox.md) geometry and the birth location is [`SCNParticleBirthLocation.vertex`](scnparticlebirthlocation/vertex.md), new particles may randomly spawn at any of the eight corners of the box.

The default value is [`SCNParticleBirthLocation.surface`](scnparticlebirthlocation/surface.md), specifying that new particles spawn at random locations along the surface of the [`emitterShape`](scnparticlesystem/emittershape.md) geometry. For possible values, see [`SCNParticleBirthLocation`](scnparticlebirthlocation.md).

## See Also

- [var emitterShape: SCNGeometry?](scnparticlesystem/emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [enum SCNParticleBirthLocation](scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](scnparticlesystem/birthlocation.md) property.
- [var birthDirection: SCNParticleBirthDirection](scnparticlesystem/birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthDirection](scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](scnparticlesystem/birthdirection.md) property.
- [var emittingDirection: SCNVector3](scnparticlesystem/emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthlocation)*