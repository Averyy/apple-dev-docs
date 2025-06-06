# fresnelExponent

**Framework**: SceneKit  
**Kind**: property

The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.

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
var fresnelExponent: CGFloat { get set }
```

#### Discussion

This property only takes effect when the [`particleImage`](scnparticlesystem/particleimage.md) property is an array of six images defining a cube map. In this case, SceneKit renders each particle as a reflective sphere.

The  modulates the reflectivity of a surface from different view angles. At the default value of `1.0`, reflections have the same intensity across the entire surface of the particle. At higher values, the edges of the particle are more reflective than the center.

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
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/fresnelexponent)*