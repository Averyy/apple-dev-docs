# orientationMode

**Framework**: SceneKit  
**Kind**: property

The mode defining whether and how particles may rotate.

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
var orientationMode: SCNParticleOrientationMode { get set }
```

#### Discussion

A particle’s angle (or orientation) is independent from its direction of motion. For example, a smoke effect may use a small image of a cloud for each particle, which stays at the same angle as the smoke rises, but a snow effect may use an image that flips and rotates as each snowflake falls.

For possible orientation modes, see [`SCNParticleOrientationMode`](scnparticleorientationmode.md). The default value is [`SCNParticleOrientationMode.billboardScreenAligned`](scnparticleorientationmode/billboardscreenaligned.md).

## See Also

- [var blendMode: SCNParticleBlendMode](scnparticlesystem/blendmode.md)
  The blending mode for compositing particle images into the rendered scene.
- [enum SCNParticleBlendMode](scnparticleblendmode.md)
  Options for combining source and destination pixel colors when compositing particles during rendering, used by the [`blendMode`](scnparticlesystem/blendmode.md) property.
- [enum SCNParticleOrientationMode](scnparticleorientationmode.md)
  Options for restricting the orientation of particles, used by the [`orientationMode`](scnparticlesystem/orientationmode.md) property.
- [var sortingMode: SCNParticleSortingMode](scnparticlesystem/sortingmode.md)
  The mode defining the order in which SceneKit renders the system’s particles.
- [enum SCNParticleSortingMode](scnparticlesortingmode.md)
  Options for the rendering order of particles, used by the [`sortingMode`](scnparticlesystem/sortingmode.md) property.
- [var isLightingEnabled: Bool](scnparticlesystem/islightingenabled.md)
  A Boolean value that determines whether SceneKit applies lighting to particle images when rendering.
- [var isBlackPassEnabled: Bool](scnparticlesystem/isblackpassenabled.md)
  A Boolean value that determines whether SceneKit renders particles in black before rendering the particle image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/orientationmode)*