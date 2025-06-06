# birthDirection

**Framework**: SceneKit  
**Kind**: property

The possible initial directions for newly spawned particles, relative to the emitter shape.

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
var birthDirection: SCNParticleBirthDirection { get set }
```

#### Discussion

This property defines initial directions for new particles relative to the geometry specified in the [`emitterShape`](scnparticlesystem/emittershape.md) property. This property has no effect if the [`emitterShape`](scnparticlesystem/emittershape.md) property value is `nil`.

For example, if the emitter shape is an [`SCNSphere`](scnsphere.md) geometry and the birth location is [`SCNParticleBirthDirection.surfaceNormal`](scnparticlebirthdirection/surfacenormal.md), new particles radiate away from the center of the sphere. You can randomize the direction of newly spawned particles with the [`spreadingAngle`](scnparticlesystem/spreadingangle.md) property.

The default value is [`SCNParticleBirthDirection.constant`](scnparticlebirthdirection/constant.md), specifying that all particles use the same base [`emittingDirection`](scnparticlesystem/emittingdirection.md) value.  For possible values, see [`SCNParticleBirthDirection`](scnparticlebirthdirection.md).

## See Also

- [var emitterShape: SCNGeometry?](scnparticlesystem/emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [var birthLocation: SCNParticleBirthLocation](scnparticlesystem/birthlocation.md)
  The possible locations for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthLocation](scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](scnparticlesystem/birthlocation.md) property.
- [enum SCNParticleBirthDirection](scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](scnparticlesystem/birthdirection.md) property.
- [var emittingDirection: SCNVector3](scnparticlesystem/emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthdirection)*