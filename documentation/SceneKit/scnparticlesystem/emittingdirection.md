# emittingDirection

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The initial direction for newly spawned particles. Animatable.

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
var emittingDirection: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 emittingDirection;
```

## Discussion

If the the [`emitterShape`](./emittershape.md) property value is `nil` or the [`birthDirection`](./birthdirection.md) property value is [`SCNParticleBirthDirection.constant`](../scnparticlebirthdirection/constant.md), newly spawned particles emit in the direction specified by this property. You can randomize the direction of newly spawned particles with the [`spreadingAngle`](./spreadingangle.md) property.

The default value is the vector `{0.0, 0.0, 1.0}`, specifying that particles emit in the direction of the positive z-axis.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Particle Emission Locations
- [var emitterShape: SCNGeometry?](./emittershape.md)
  The shape of the region of space where the system spawns new particles.
- [var birthLocation: SCNParticleBirthLocation](./birthlocation.md)
  The possible locations for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthLocation](../scnparticlebirthlocation.md)
  Options for the initial location of each emitted particle, used by the [`birthLocation`](./birthlocation.md) property.
- [var birthDirection: SCNParticleBirthDirection](./birthdirection.md)
  The possible initial directions for newly spawned particles, relative to the emitter shape.
- [enum SCNParticleBirthDirection](../scnparticlebirthdirection.md)
  Options for the initial direction of each emitted particle, used by the [`birthDirection`](./birthdirection.md) property.
- [var spreadingAngle: CGFloat](./spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/emittingdirection)*