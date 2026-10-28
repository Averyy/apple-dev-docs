# mappingChannel

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The source of texture coordinates for mapping the material property’s image contents.

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
var mappingChannel: Int { get set }
```

```objc
@property (nonatomic) NSInteger mappingChannel;
```

## Discussion

A geometry can have multiple independent sources of texture coordinates, each of which defines a unique mapping channel number. You can use these channels to map different visual properties of a material in different ways. For example, a geometry representing a picture frame might use one set of texture coordinates for mapping the materials of the frame itself, and another set of texture coordinates for placing a picture into the frame.

For information about creating geometries with multiple texture mapping channels, see [`SCNGeometry`](../scngeometry.md).

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
- [var maxAnisotropy: CGFloat](./maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var borderColor: Any?](./bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/mappingchannel)*