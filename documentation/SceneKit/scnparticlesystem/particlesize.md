# particleSize

**Framework**: SceneKit  
**Kind**: property

The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.

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
var particleSize: CGFloat { get set }
```

#### Discussion

SceneKit uses this value for both the width and height of the [`particleImage`](scnparticlesystem/particleimage.md) texture at render time. (If you use the [`stretchFactor`](scnparticlesystem/stretchfactor.md) property to stretch particles in their direction of motion, the [`particleSize`](scnparticlesystem/particlesize.md) value determines the width and height before stretching.) You can randomize the sizes of newly spawned particles with the [`particleSizeVariation`](scnparticlesystem/particlesizevariation.md) property.

The default value is `1.0`, specifying that particle images appear one unit high and one unit wide in the scene’s world coordinate space.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

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
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlesize)*