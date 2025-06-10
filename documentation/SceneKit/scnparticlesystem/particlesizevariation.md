# particleSizeVariation

**Framework**: SceneKit  
**Kind**: property

The range of randomized particle sizes. Animatable.

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
var particleSizeVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`particleSize`](scnparticlesystem/particlesize.md) property. SceneKit randomly adjusts the size of each particle by up to half the [`particleSizeVariation`](scnparticlesystem/particlesizevariation.md) value. For example, if the [`particleSize`](scnparticlesystem/particlesize.md) value is `1.0` and the [`particleSizeVariation`](scnparticlesystem/particlesizevariation.md) value is `0.5`, newly spawned particles are randomly sized between `0.75` and `1.25` units wide and high.

The default value is `0.0`, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleSize: CGFloat](scnparticlesystem/particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleColor: UIColor](scnparticlesystem/particlecolor.md)
  The color of newly spawned particles. Animatable.
- [var particleColorVariation: SCNVector4](scnparticlesystem/particlecolorvariation.md)
  The ranges of randomized particle color components. Animatable.
- [var particleImage: Any?](scnparticlesystem/particleimage.md)
  The texture image SceneKit uses to render each particle.
- [var fresnelExponent: CGFloat](scnparticlesystem/fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlesizevariation)*