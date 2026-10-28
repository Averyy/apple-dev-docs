# isBlackPassEnabled

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit renders particles in black before rendering the particle image.

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
var isBlackPassEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isBlackPassEnabled) BOOL blackPassEnabled;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) to enhance visual contrast when using additive blending. The default value is [`false`](../../Swift/false.md).

> ❗ **Important**:  Because a black pass requires rendering the entire particle system twice, enabling this option can severely affect rendering performance.

## See Also

### Managing Particle Rendering
- [var blendMode: SCNParticleBlendMode](./blendmode.md)
  The blending mode for compositing particle images into the rendered scene.
- [enum SCNParticleBlendMode](../scnparticleblendmode.md)
  Options for combining source and destination pixel colors when compositing particles during rendering, used by the [`blendMode`](./blendmode.md) property.
- [var orientationMode: SCNParticleOrientationMode](./orientationmode.md)
  The mode defining whether and how particles may rotate.
- [enum SCNParticleOrientationMode](../scnparticleorientationmode.md)
  Options for restricting the orientation of particles, used by the [`orientationMode`](./orientationmode.md) property.
- [var sortingMode: SCNParticleSortingMode](./sortingmode.md)
  The mode defining the order in which SceneKit renders the system’s particles.
- [enum SCNParticleSortingMode](../scnparticlesortingmode.md)
  Options for the rendering order of particles, used by the [`sortingMode`](./sortingmode.md) property.
- [var isLightingEnabled: Bool](./islightingenabled.md)
  A Boolean value that determines whether SceneKit applies lighting to particle images when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/isblackpassenabled)*