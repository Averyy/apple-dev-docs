# SCNFilterMode

**Framework**: SceneKit  
**Kind**: enum

Texture filtering modes, used by the [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md), and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum SCNFilterMode
```

#### Overview

Texture filtering determines the appearance of a material property’s contents when portions of the material surface appear larger or smaller than the original texture image. For example, when a texture is applied to a plane that recedes away from the camera into the distance:

- The texture coordinates at a point near the camera may correspond to a small fraction of a pixel in the original image. SceneKit uses the [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md) property to determine the color of the sampled texel at that point.
- The texture coordinates at a point far from the camera may correspond to an area of several pixels in the original image. SceneKit uses the [`minificationFilter`](scnmaterialproperty/minificationfilter.md) property to determine the color of the sampled texel at that point.

SceneKit also uses the filter specified by the [`mipFilter`](scnmaterialproperty/mipfilter.md) property when generating mipmap levels for a texture image.

## Topics

### Constants
- [SCNFilterMode.none](scnfiltermode/none.md)
  No texture filtering is applied.
- [SCNFilterMode.nearest](scnfiltermode/nearest.md)
  Texture filtering returns the color from only one texel, whose location is nearest to the coordinates being sampled.
- [SCNFilterMode.linear](scnfiltermode/linear.md)
  Texture filtering sample texels from the neighborhood of the coordinates being sampled and linearly interpolates their colors.
### Initializers
- [init?(rawValue: Int)](scnfiltermode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var contentsTransform: SCNMatrix4](scnmaterialproperty/contentstransform.md)
  The transformation applied to the material property’s visual contents. Animatable.
- [var wrapS: SCNWrapMode](scnmaterialproperty/wraps.md)
  The wrapping behavior for the S texture coordinate.
- [var wrapT: SCNWrapMode](scnmaterialproperty/wrapt.md)
  The wrapping behavior for the T texture coordinate.
- [enum SCNWrapMode](scnwrapmode.md)
  Modes to apply to texture wrapping, used by the [`wrapT`](scnmaterialproperty/wrapt.md) and [`wrapS`](scnmaterialproperty/wraps.md) properties.
- [var minificationFilter: SCNFilterMode](scnmaterialproperty/minificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size smaller than that of the original image.
- [var magnificationFilter: SCNFilterMode](scnmaterialproperty/magnificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size larger than that of the original image.
- [var mipFilter: SCNFilterMode](scnmaterialproperty/mipfilter.md)
  Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.
- [var maxAnisotropy: CGFloat](scnmaterialproperty/maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfiltermode)*