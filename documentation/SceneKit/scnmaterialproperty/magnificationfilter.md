# magnificationFilter

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

Texture filtering for rendering the material property’s image contents at a size larger than that of the original image.

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
var magnificationFilter: SCNFilterMode { get set }
```

```objc
@property (nonatomic) SCNFilterMode magnificationFilter;
```

#### Discussion

Texture filtering determines the appearance of a material property’s contents when portions of the material surface appear larger or smaller than the original texture image. For example, the texture coordinates at a point near the camera may correspond to a small fraction of a pixel in the texture image. SceneKit uses the magnification filter to determine the color of the sampled texel at that point.

The default magnification filter is [`SCNFilterMode.linear`](../scnfiltermode/linear.md). See [`SCNWrapMode`](../scnwrapmode.md) for available modes and their effects.

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
- [var mipFilter: SCNFilterMode](./mipfilter.md)
  Texture filtering for using mipmaps to render the material property’s image contents at a size smaller than that of the original image.
- [enum SCNFilterMode](../scnfiltermode.md)
  Texture filtering modes, used by the [`minificationFilter`](./minificationfilter.md), [`magnificationFilter`](./magnificationfilter.md), and [`mipFilter`](./mipfilter.md) properties.
- [var maxAnisotropy: CGFloat](./maxanisotropy.md)
  The amount of anisotropic texture filtering to be used when rendering the material property’s image contents.
- [var mappingChannel: Int](./mappingchannel.md)
  The source of texture coordinates for mapping the material property’s image contents.
- [var borderColor: Any?](./bordercolor.md)
  A color used to fill in areas of a material’s surface not covered by the material property’s image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/magnificationfilter)*