# particleColorVariation

**Framework**: SceneKit  
**Kind**: property

The ranges of randomized particle color components. Animatable.

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
var particleColorVariation: SCNVector4 { get set }
```

#### Discussion

This vector randomizes the color specified by the [`particleColor`](scnparticlesystem/particlecolor.md) property. The components of the vector specify ranges of variation in hue, saturation, brightness, and alpha, in that order.

For example, consider the effects of different [`particleColorVariation`](scnparticlesystem/particlecolorvariation.md) vectors on a system whose [`particleColor`](scnparticlesystem/particlecolor.md) property specifies a fully opaque red as the base color:

- The vector `{0.25, 0.0, 0.0, 0.0}` allows newly spawned particles to take on any hue within a quarter of the color wheel centered on red (that is, ranging from purple through magenta, red, orange, and yellow to green). Particles retain full saturation, brightness, and alpha.
- The vector `{0.0, 0.0, 0.0, 1.0}` allows newly spawned particles to vary in alpha between full and half opacity. (The range of variation is centered on the base value, but clamped to a maximum of `1.0`.) Particles retain the same hue, saturation, and brightness as the base color.
- The vector `{0.0, 1.0, 1.0, 0.0}` allows newly spawned particles to vary in saturation and brightness, resulting in random shades of red. Particles retain the same hue and alpha as the base color.

The default value is [`SCNVector4Zero`](scnvector4zero.md), specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleSize: CGFloat](scnparticlesystem/particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleSizeVariation: CGFloat](scnparticlesystem/particlesizevariation.md)
  The range of randomized particle sizes. Animatable.
- [var particleColor: UIColor](scnparticlesystem/particlecolor.md)
  The color of newly spawned particles. Animatable.
- [var particleImage: Any?](scnparticlesystem/particleimage.md)
  The texture image SceneKit uses to render each particle.
- [var fresnelExponent: CGFloat](scnparticlesystem/fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlecolorvariation)*