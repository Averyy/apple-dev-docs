# SCNParticleOrientationMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for restricting the orientation of particles, used by the [`orientationMode`](./scnparticlesystem/orientationmode.md) property.

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
enum SCNParticleOrientationMode
```

```c
enum SCNParticleOrientationMode : NSInteger;
```

## Topics

### Constants
- [SCNParticleOrientationMode.billboardScreenAligned](./scnparticleorientationmode/billboardscreenaligned.md)
  Each particle’s orientation is always fixed with respect to the point of view camera.
- [SCNParticleOrientationMode.billboardViewAligned](./scnparticleorientationmode/billboardviewaligned.md)
  Each particle always faces the point of view camera (but may rotate about an axis parallel to the view direction).
- [SCNParticleOrientationMode.free](./scnparticleorientationmode/free.md)
  Particle orientations are not restricted; they may rotate freely in all axes.
- [SCNParticleOrientationMode.billboardYAligned](./scnparticleorientationmode/billboardyaligned.md)
  The y-axis direction of each particle is always fixed with respect to the point of view camera.
### Initializers
- [init?(rawValue: Int)](./scnparticleorientationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Particle Rendering
- [var blendMode: SCNParticleBlendMode](./scnparticlesystem/blendmode.md)
  The blending mode for compositing particle images into the rendered scene.
- [enum SCNParticleBlendMode](./scnparticleblendmode.md)
  Options for combining source and destination pixel colors when compositing particles during rendering, used by the [`blendMode`](./scnparticlesystem/blendmode.md) property.
- [var orientationMode: SCNParticleOrientationMode](./scnparticlesystem/orientationmode.md)
  The mode defining whether and how particles may rotate.
- [var sortingMode: SCNParticleSortingMode](./scnparticlesystem/sortingmode.md)
  The mode defining the order in which SceneKit renders the system’s particles.
- [enum SCNParticleSortingMode](./scnparticlesortingmode.md)
  Options for the rendering order of particles, used by the [`sortingMode`](./scnparticlesystem/sortingmode.md) property.
- [var isLightingEnabled: Bool](./scnparticlesystem/islightingenabled.md)
  A Boolean value that determines whether SceneKit applies lighting to particle images when rendering.
- [var isBlackPassEnabled: Bool](./scnparticlesystem/isblackpassenabled.md)
  A Boolean value that determines whether SceneKit renders particles in black before rendering the particle image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleorientationmode)*