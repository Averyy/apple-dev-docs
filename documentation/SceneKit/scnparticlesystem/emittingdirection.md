# emittingDirection

**Framework**: SceneKit  
**Kind**: property

The initial direction for newly spawned particles. Animatable.

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
var emittingDirection: SCNVector3 { get set }
```

#### Discussion

If the the [`emitterShape`](scnparticlesystem/emittershape.md) property value is `nil` or the [`birthDirection`](scnparticlesystem/birthdirection.md) property value is [`SCNParticleBirthDirection.constant`](scnparticlebirthdirection/constant.md), newly spawned particles emit in the direction specified by this property. You can randomize the direction of newly spawned particles with the [`spreadingAngle`](scnparticlesystem/spreadingangle.md) property.

The default value is the vector `{0.0, 0.0, 1.0}`, specifying that particles emit in the direction of the positive z-axis.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var emitterShape: SCNGeometry?](scnparticlesystem/emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [var birthLocation: SCNParticleBirthLocation](scnparticlesystem/birthlocation.md)
  The possible locations for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthLocation](scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](scnparticlesystem/birthlocation.md) property.
- [var birthDirection: SCNParticleBirthDirection](scnparticlesystem/birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthDirection](scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](scnparticlesystem/birthdirection.md) property.
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/emittingdirection)*