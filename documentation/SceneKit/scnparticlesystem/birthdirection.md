# birthDirection

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The possible initial directions for newly spawned particles, relative to the emitter shape.

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
var birthDirection: SCNParticleBirthDirection { get set }
```

```objc
@property (nonatomic) SCNParticleBirthDirection birthDirection;
```

## Discussion

This property defines initial directions for new particles relative to the geometry specified in the [`emitterShape`](./emittershape.md) property. This property has no effect if the [`emitterShape`](./emittershape.md) property value is `nil`.

For example, if the emitter shape is an [`SCNSphere`](../scnsphere.md) geometry and the birth location is [`SCNParticleBirthDirection.surfaceNormal`](../scnparticlebirthdirection/surfacenormal.md), new particles radiate away from the center of the sphere. You can randomize the direction of newly spawned particles with the [`spreadingAngle`](./spreadingangle.md) property.

The default value is [`SCNParticleBirthDirection.constant`](../scnparticlebirthdirection/constant.md), specifying that all particles use the same base [`emittingDirection`](./emittingdirection.md) value.  For possible values, see [`SCNParticleBirthDirection`](../scnparticlebirthdirection.md).

## See Also

### Managing Particle Emission Locations
- [var emitterShape: SCNGeometry?](./emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [var birthLocation: SCNParticleBirthLocation](./birthlocation.md)
  The possible locations for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthLocation](../scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](./birthlocation.md) property.
- [enum SCNParticleBirthDirection](../scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](./birthdirection.md) property.
- [var emittingDirection: SCNVector3](./emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.
- [var spreadingAngle: CGFloat](./spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/birthdirection)*