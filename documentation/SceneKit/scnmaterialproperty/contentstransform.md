# contentsTransform

**Framework**: SceneKit  
**Kind**: property

The transformation applied to the material property’s visual contents. Animatable.

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
var contentsTransform: SCNMatrix4 { get set }
```

#### Discussion

SceneKit applies this transformation to the texture coordinates provided by the geometry object the material is attached to, then uses the resulting coordinates to map the material property’s [`contents`](scnmaterialproperty/contents.md) across the surface of the material. (This transformation has no effect if the material property’s [`contents`](scnmaterialproperty/contents.md) object is a constant color.)

For example, you can use this property to grow, offset, or rotate a texture relative to the surface of a material, as illustrated below.

![None](https://docs-assets.developer.apple.com/published/378b1d77e45a8491465a75f8a83982d8/media-2929785%402x.png)

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

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
- [var maxAnisotropy: CGFloat](scnmaterialproperty/maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](scnmaterialproperty/mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](scnmaterialproperty/bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/contentstransform)*