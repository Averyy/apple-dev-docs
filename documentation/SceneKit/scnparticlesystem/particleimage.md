# particleImage

**Framework**: SceneKit  
**Kind**: property

The texture image SceneKit uses to render each particle.

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
var particleImage: Any? { get set }
```

#### Discussion

Texture images help to determine visual effect rendered by the particle system. The [`particleColor`](scnparticlesystem/particlecolor.md) property colorizes the image before rendering. You may specify an image using an [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) (in macOS) or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) (in iOS) instance, or an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) instance containing the path or URL to an image file.

If the value is `nil` (the default), SceneKit renders each particle as a small white square (colorized by the [`particleColor`](scnparticlesystem/particlecolor.md) property).

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [`Figure 1`](scnparticlesystem/1524153-particleimage#1965925.md), then use the properties listed in Animating Particle Images to identify frames in the grid and set the speed and style of the animation.

![None](https://docs-assets.developer.apple.com/published/fac5a79830660a448a39b7b503f41e60/media-1965925%402x.png)

You can also create particles that appear reflective by assigning an array of images to this property. SceneKit treats the six images in the array as a cube map and renders each particle as a solid-color, reflective sphere. The particle system’s [`fresnelExponent`](scnparticlesystem/fresnelexponent.md) property controls each sphere’s reflectivity. For details on cube map textures, see [`SCNMaterialProperty`](scnmaterialproperty.md).

## See Also

- [var particleSize: CGFloat](scnparticlesystem/particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleSizeVariation: CGFloat](scnparticlesystem/particlesizevariation.md)
  The range of randomized particle sizes. Animatable.
- [var particleColor: UIColor](scnparticlesystem/particlecolor.md)
  The color of newly spawned particles. Animatable.
- [var particleColorVariation: SCNVector4](scnparticlesystem/particlecolorvariation.md)
  The ranges of randomized particle color components. Animatable.
- [var fresnelExponent: CGFloat](scnparticlesystem/fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.
- [var stretchFactor: CGFloat](scnparticlesystem/stretchfactor.md)
  A multiplier for stretching particle images along their direction of motion. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/particleimage)*