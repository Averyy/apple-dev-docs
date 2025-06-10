# maxAnisotropy

**Framework**: SceneKit  
**Kind**: property

The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.

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
var maxAnisotropy: CGFloat { get set }
```

#### Discussion

Anisotropic filtering is a process that increases the quality of texture rendering when a textured surface appears at an extreme angle relative to the camera. This process works by sampling from multiple mipmap levels of a texture for each rendered pixel—the term anisotropy refers to the number of samples per pixel. A higher anisotropy improves rendering quality, but at a cost to rendering performance.

For example, the image on the left in the figure below uses no anisotropic filtering, resulting in rendering artifacts as the checkerboard pattern recedes into the distance. The other images use higher [`maxAnisotropy`](scnmaterialproperty/maxanisotropy.md) values, reducing rendering artifacts. Anisotropic filtering requires mipmaps, so this property only takes effect if the value of the [`mipFilter`](scnmaterialproperty/mipfilter.md) property is not [`SCNFilterMode.none`](scnfiltermode/none.md).

![None](https://docs-assets.developer.apple.com/published/8fc5eb20217d242fe7b3f882a919fee0/media-2929776%402x.png)

SceneKit automatically increases or decreases anisotropy for each rendered pixel as needed to maximize rendering quality, up to the limit specified by this property. The maximum anisotropy level used when rendering is dependent on the graphics hardware in use. Set this property’s value to the `MAXFLOAT` constant (the default) to use the highest anisotropy level supported by the GPU. A [`maxAnisotropy`](scnmaterialproperty/maxanisotropy.md) value of `1.0` or lower disables anisotropic filtering.

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
- [enum SCNFilterMode](scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md), and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/maxanisotropy)*