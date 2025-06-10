# minificationFilter

**Framework**: SceneKit  
**Kind**: property

Texture filtering for rendering the material property’s image contents at a size smaller than that of the original image.

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
var minificationFilter: SCNFilterMode { get set }
```

#### Discussion

Texture filtering determines the appearance of a material property’s contents when portions of the material surface appear larger or smaller than the original texture image. For example, the texture coordinates at a point far from the camera may correspond to an area of several pixels in the texture image. SceneKit uses the minification filter to determine the color of the sampled texel at that point.

The default minification filter is [`SCNFilterMode.linear`](scnfiltermode/linear.md). See [`SCNWrapMode`](scnwrapmode.md) for available modes and their effects.

## See Also

- [var contentsTransform: SCNMatrix4](scnmaterialproperty/contentstransform.md)
  The transformation applied to the material property’s visual contents. Animatable.
- [var wrapS: SCNWrapMode](scnmaterialproperty/wraps.md)
  The wrapping behavior for the S texture coordinate.
- [var wrapT: SCNWrapMode](scnmaterialproperty/wrapt.md)
  The wrapping behavior for the T texture coordinate.
- [enum SCNWrapMode](scnwrapmode.md)
  Modes to apply to texture wrapping, used by the [`wrapT`](scnmaterialproperty/wrapt.md) and [`wrapS`](scnmaterialproperty/wraps.md) properties.
- [var magnificationFilter: SCNFilterMode](scnmaterialproperty/magnificationfilter.md)
  Texture filtering for rendering the material property’s image contents at a size larger than that of the original image.
- [var mipFilter: SCNFilterMode](scnmaterialproperty/mipfilter.md)
  Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.
- [enum SCNFilterMode](scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md), and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties.
- [var maxAnisotropy: CGFloat](scnmaterialproperty/maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/minificationfilter)*