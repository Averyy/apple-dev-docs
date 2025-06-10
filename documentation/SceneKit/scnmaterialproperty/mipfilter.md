# mipFilter

**Framework**: SceneKit  
**Kind**: property

Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.

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
var mipFilter: SCNFilterMode { get set }
```

#### Discussion

Mipmapping is a technique that can increase rendering performance when rendering a texture image at smaller sizes. SceneKit automatically creates several mipmap levels for the material property’s image contents, each at a fraction of the original image’s size. When rendering, SceneKit automatically samples texels from the mipmap level closest to the size being rendered.

If the value of this property is [`SCNFilterMode.none`](scnfiltermode/none.md), SceneKit does not use mipmapping. If the value of this property is [`SCNFilterMode.linear`](scnfiltermode/linear.md), SceneKit determines pixel colors using trilinear filtering. First it linearly interpolates a texel color from each of the two mipmap levels closest to the target size, then it linearly interpolates between the two results to determine the final color. This technique provides higher rendering quality at moderate performance cost.

In iOS 10, tvOS 10, watchOS 3, and macOS 10.12, the default mipmapping filter mode is [`SCNFilterMode.nearest`](scnfiltermode/nearest.md). In earlier OS versions, the default mode is [`SCNFilterMode.none`](scnfiltermode/none.md).

The figure below shows the effects of enabling mipmapping. In the image on the left, mipmapping is disabled, causing pixelated artifacts as the checkerboard pattern recedes into the distance. Enabling linear mipmapping results in a smoother appearance.

![None](https://docs-assets.developer.apple.com/published/8fc5eb20217d242fe7b3f882a919fee0/media-2929775%402x.png)

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
- [enum SCNFilterMode](scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md), and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties.
- [var maxAnisotropy: CGFloat](scnmaterialproperty/maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/mipfilter)*