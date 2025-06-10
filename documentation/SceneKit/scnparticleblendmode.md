# SCNParticleBlendMode

**Framework**: SceneKit  
**Kind**: enum

Options for combining source and destination pixel colors when compositing particles during rendering, used by the [`blendMode`](scnparticlesystem/blendmode.md) property.

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
enum SCNParticleBlendMode
```

## Topics

### Constants
- [SCNParticleBlendMode.additive](scnparticleblendmode/additive.md)
  The source and destination colors are added together.
- [SCNParticleBlendMode.subtract](scnparticleblendmode/subtract.md)
  The source color is subtracted from the destination color.
- [SCNParticleBlendMode.multiply](scnparticleblendmode/multiply.md)
  The source color is multiplied by the destination color.
- [SCNParticleBlendMode.screen](scnparticleblendmode/screen.md)
  The source color is added to the destination color times the inverted source color.
- [SCNParticleBlendMode.alpha](scnparticleblendmode/alpha.md)
  The source and destination colors are blended by multiplying the source alpha value.
- [SCNParticleBlendMode.replace](scnparticleblendmode/replace.md)
  The source color replaces the destination color.
### Initializers
- [init?(rawValue: Int)](scnparticleblendmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var blendMode: SCNParticleBlendMode](scnparticlesystem/blendmode.md)
  The blending mode for compositing particle images into the rendered scene.
- [var orientationMode: SCNParticleOrientationMode](scnparticlesystem/orientationmode.md)
  The mode defining whether and how particles may rotate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleblendmode)*