# particleColor

**Framework**: SceneKit  
**Kind**: property

The color of newly spawned particles. Animatable.

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
var particleColor: UIColor { get set }
```

#### Discussion

This color tints or shades the texture provided by the [`particleImage`](scnparticlesystem/particleimage.md) property. You can use this property to implement a range of many possible visual effects using the same artwork. For example, a small, blurry, white circle texture can be tinted yellow or orange to simulate fire, shaded gray or black to simulate smoke, or left alone to simulate falling snow.

The default color is white, causing the particle image to appear without tint or shading.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var particleSize: CGFloat](scnparticlesystem/particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleSizeVariation: CGFloat](scnparticlesystem/particlesizevariation.md)
  The range of randomized particle sizes. Animatable.
- [var particleColorVariation: SCNVector4](scnparticlesystem/particlecolorvariation.md)
  The ranges of randomized particle color components. Animatable.
- [var particleImage: Any?](scnparticlesystem/particleimage.md)
  The texture image SceneKit uses to render each particle.
- [var fresnelExponent: CGFloat](scnparticlesystem/fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particlecolor)*