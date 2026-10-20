# maxAnisotropy

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var maxAnisotropy: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat maxAnisotropy;
```

#### Discussion

Anisotropic filtering is a process that increases the quality of texture rendering when a textured surface appears at an extreme angle relative to the camera. This process works by sampling from multiple mipmap levels of a texture for each rendered pixel—the term anisotropy refers to the number of samples per pixel. A higher anisotropy improves rendering quality, but at a cost to rendering performance.

For example, the image on the left in the figure below uses no anisotropic filtering, resulting in rendering artifacts as the checkerboard pattern recedes into the distance. The other images use higher [`maxAnisotropy`](./maxanisotropy.md) values, reducing rendering artifacts. Anisotropic filtering requires mipmaps, so this property only takes effect if the value of the [`mipFilter`](./mipfilter.md) property is not [`SCNFilterMode.none`](../scnfiltermode/none.md).

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929776@2x.png)

SceneKit automatically increases or decreases anisotropy for each rendered pixel as needed to maximize rendering quality, up to the limit specified by this property. The maximum anisotropy level used when rendering is dependent on the graphics hardware in use. Set this property’s value to the `MAXFLOAT` constant (the default) to use the highest anisotropy level supported by the GPU. A [`maxAnisotropy`](./maxanisotropy.md) value of `1.0` or lower disables anisotropic filtering.

## See Also

### Configuring Texture Mapping Attributes
- [var contentsTransform: SCNMatrix4](./contentstransform.md)
  The transformation applied to the material property’s visual contents. Animatable.
- [var wrapS: SCNWrapMode](./wraps.md)
  The wrapping behavior for the S texture coordinate.
- [var wrapT: SCNWrapMode](./wrapt.md)
  The wrapping behavior for the T texture coordinate.
- [enum SCNWrapMode](../scnwrapmode.md)
  Modes to apply to texture wrapping, used by the [`wrapT`](./wrapt.md) and [`wrapS`](./wraps.md) properties.
- [var minificationFilter: SCNFilterMode](./minificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size smaller than that of the original image.
- [var magnificationFilter: SCNFilterMode](./magnificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size larger than that of the original image.
- [var mipFilter: SCNFilterMode](./mipfilter.md)
  Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.
- [enum SCNFilterMode](../scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](./minificationfilter.md), [`magnificationFilter`](./magnificationfilter.md), and [`mipFilter`](./mipfilter.md) properties.
- [var mappingChannel: Int](./mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](./bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/maxanisotropy)*