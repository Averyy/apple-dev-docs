# stretchFactor

**Framework**: SceneKit  
**Kind**: property

A multiplier for stretching particle images along their direction of motion. Animatable.

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
var stretchFactor: CGFloat { get set }
```

#### Discussion

Use this property to create visual effects that show streaks of motion, such as fireworks. If the [`orientationMode`](scnparticlesystem/orientationmode.md) property value is [`SCNParticleOrientationMode.free`](scnparticleorientationmode/free.md), a non-default stretch factor stretches particle images in the y-axis direction of each particle’s local coordinate space.

The default value is `0.0`, specifying that particle images maintain their original aspect ratio.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleSize: CGFloat](scnparticlesystem/particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleSizeVariation: CGFloat](scnparticlesystem/particlesizevariation.md)
  The range of randomized particle sizes. Animatable.
- [var particleColor: UIColor](scnparticlesystem/particlecolor.md)
  The color of newly spawned particles. Animatable.
- [var particleColorVariation: SCNVector4](scnparticlesystem/particlecolorvariation.md)
  The ranges of randomized particle color components. Animatable.
- [var particleImage: Any?](scnparticlesystem/particleimage.md)
  The texture image SceneKit uses to render each particle.
- [var fresnelExponent: CGFloat](scnparticlesystem/fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/stretchfactor)*