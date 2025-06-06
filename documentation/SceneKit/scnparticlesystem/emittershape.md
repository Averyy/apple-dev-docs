# emitterShape

**Framework**: Scenekit  
**Kind**: property

The shape of the region of space where the system spawns new particles.

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
var emitterShape: SCNGeometry? { get set }
```

#### Discussion

To randomize the locations where new particles spawn, assign a geometry to this property. This geometry defines the shape of the space where new particles may spawn, and the [`birthLocation`](scnparticlesystem/birthlocation.md) and [`birthDirection`](scnparticlesystem/birthdirection.md) properties define locations within and directions relative to the shape. For example, assigning a sphere geometry causes particles to spawn at random locations along the surface of the sphere (or within the volume of the sphere, according to the [`birthLocation`](scnparticlesystem/birthlocation.md) property).

> **Note**:  For best results, use an instance of one of the SceneKit basic geometry classes ([`SCNPlane`](scnplane.md), [`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), [`SCNCapsule`](scncapsule.md), [`SCNTube`](scntube.md), and [`SCNTorus`](scntorus.md)). These classes provide a more efficient simulation and more even appearance to the rendered particle system.

The default value is `nil`, specifying that all new particles emit from a single point. For particle systems attached to a node, this point is the origin of the node’s coordinate system. For particle systems attached directly to a scene using the [`addParticleSystem(_:transform:)`](scnscene/addparticlesystem(_:transform:).md) method, use that method’s `transform` parameter to specify the emission point.

## See Also

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
- [var spreadingAngle: CGFloat](scnparticlesystem/spreadingangle.md)
  The range, in degrees, of randomized initial particle directions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/emittershape)*