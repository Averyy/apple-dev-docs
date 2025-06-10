# spreadingAngle

**Framework**: SceneKit  
**Kind**: property

The range, in degrees, of randomized initial particle directions. Animatable.

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
var spreadingAngle: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the direction specified by the [`emittingDirection`](scnparticlesystem/emittingdirection.md) or [`birthDirection`](scnparticlesystem/birthdirection.md) property. For example, at the default value of `0.0` degrees, all particles emit in the same direction. Increasing the spreading angle to `30.0` degrees allows particles to emit in any direction within a space shaped like a cone whose central angle is 30°.

This property has no effect if the [`birthDirection`](scnparticlesystem/birthdirection.md) property value is [`SCNParticleBirthDirection.random`](scnparticlebirthdirection/random.md).

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
- [var emittingDirection: SCNVector3](scnparticlesystem/emittingdirection.md)
  The initial direction for newly spawned particles. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/spreadingangle)*