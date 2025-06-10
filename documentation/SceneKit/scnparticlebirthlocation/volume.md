# SCNParticleBirthLocation.volume

**Framework**: SceneKit  
**Kind**: case

New particles can be created at any location within the volume of the emitter shape.

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
case volume
```

#### Discussion

This value applies only when the [`emitterShape`](scnparticlesystem/emittershape.md) property specifies one of SceneKit’s built-in basic geometries ([`SCNPlane`](scnplane.md), [`SCNBox`](scnbox.md), [`SCNSphere`](scnsphere.md), [`SCNPyramid`](scnpyramid.md), [`SCNCone`](scncone.md), [`SCNCylinder`](scncylinder.md), [`SCNCapsule`](scncapsule.md), [`SCNTube`](scntube.md), and [`SCNTorus`](scntorus.md)).

## See Also

- [SCNParticleBirthLocation.surface](scnparticlebirthlocation/surface.md)
  New particles can be created at any location on the surface of the emitter shape.
- [SCNParticleBirthLocation.vertex](scnparticlebirthlocation/vertex.md)
  New particles can be created at only at the locations of the vertices in the emitter shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlebirthlocation/volume)*