# birthLocation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The possible locations for newly spawned particles, relative to the emitter shape.

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
var birthLocation: SCNParticleBirthLocation { get set }
```

```objc
@property (nonatomic) SCNParticleBirthLocation birthLocation;
```

#### Discussion

This property defines locations for spawning new particles relative to the geometry specified in the [`emitterShape`](./emittershape.md) property. This property has no effect if the [`emitterShape`](./emittershape.md) property value is `nil`.

For example, if the emitter shape is an [`SCNBox`](../scnbox.md) geometry and the birth location is [`SCNParticleBirthLocation.vertex`](../scnparticlebirthlocation/vertex.md), new particles may randomly spawn at any of the eight corners of the box.

The default value is [`SCNParticleBirthLocation.surface`](../scnparticlebirthlocation/surface.md), specifying that new particles spawn at random locations along the surface of the [`emitterShape`](./emittershape.md) geometry. For possible values, see [`SCNParticleBirthLocation`](../scnparticlebirthlocation.md).

## See Also

### Managing Particle Emission Locations
- [var emitterShape: SCNGeometry?](./emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [enum SCNParticleBirthLocation](../scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](./birthlocation.md) property.
- [var birthDirection: SCNParticleBirthDirection](./birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthDirection](../scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](./birthdirection.md) property.
- [var emittingDirection: SCNVector3](./emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](./spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthlocation)*