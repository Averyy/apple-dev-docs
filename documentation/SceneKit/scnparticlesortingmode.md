# SCNParticleSortingMode

**Framework**: SceneKit  
**Kind**: enum

Options for the rendering order of particles, used by the [`sortingMode`](scnparticlesystem/sortingmode.md) property.

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
enum SCNParticleSortingMode
```

## Topics

### Constants
- [SCNParticleSortingMode.none](scnparticlesortingmode/none.md)
  Particles are not sorted; they may be rendered in any order.
- [SCNParticleSortingMode.projectedDepth](scnparticlesortingmode/projecteddepth.md)
  Particles farther from the point of view (as measured using projected depth) are rendered before closer particles.
- [SCNParticleSortingMode.distance](scnparticlesortingmode/distance.md)
  Particles farther from the point of view (as measured using distance from the camera in scene space) are rendered before closer particles.
- [SCNParticleSortingMode.oldestFirst](scnparticlesortingmode/oldestfirst.md)
  Particles emitted earlier are rendered before particles emitted more recently.
- [SCNParticleSortingMode.youngestFirst](scnparticlesortingmode/youngestfirst.md)
  Particles emitted more recently are rendered before particles emitted earlier.
### Initializers
- [init?(rawValue: Int)](scnparticlesortingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var blendMode: SCNParticleBlendMode](scnparticlesystem/blendmode.md)
  The blending mode for compositing particle images into the rendered scene.
- [enum SCNParticleBlendMode](scnparticleblendmode.md)
  Options for combining source and destination pixel colors when compositing particles during rendering, used by the [`blendMode`](scnparticlesystem/blendmode.md) property.
- [var orientationMode: SCNParticleOrientationMode](scnparticlesystem/orientationmode.md)
  The mode defining whether and how particles may rotate.
- [enum SCNParticleOrientationMode](scnparticleorientationmode.md)
  Options for restricting the orientation of particles, used by the [`orientationMode`](scnparticlesystem/orientationmode.md) property.
- [var sortingMode: SCNParticleSortingMode](scnparticlesystem/sortingmode.md)
  The mode defining the order in which SceneKit renders the system’s particles.
- [var isLightingEnabled: Bool](scnparticlesystem/islightingenabled.md)
  A Boolean value that determines whether SceneKit applies lighting to particle images when rendering.
- [var isBlackPassEnabled: Bool](scnparticlesystem/isblackpassenabled.md)
  A Boolean value that determines whether SceneKit renders particles in black before rendering the particle image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesortingmode)*