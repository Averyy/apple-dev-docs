# isLightingEnabled

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit applies lighting to particle images when rendering.

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
var isLightingEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isLightingEnabled) BOOL lightingEnabled;
```

#### Discussion

If [`true`](../../Swift/true.md), SceneKit uses the position, color, and other attributes of [`SCNLight`](../scnlight.md) objects in the scene to shade each rendered particle image. Use this option to enhance volumetric effects such as smoke and fog.

The default value is [`false`](../../Swift/false.md).

> **Note**:  SceneKit uses only one [`SCNLight`](../scnlight.md) object to illuminate rendered particles. Use the [`categoryBitMask`](../scnnode/categorybitmask.md) of the node containing the particle system to control which light applies to the particles.

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
- [var isBlackPassEnabled: Bool](./isblackpassenabled.md)
  A Boolean value that determines whether SceneKit renders particles in black before rendering the particle image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/islightingenabled)*