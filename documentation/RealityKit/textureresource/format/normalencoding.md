# TextureResource.Format.NormalEncoding

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

A profile that specifies the interpretation of pixel values as a normal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum NormalEncoding
```

## Topics

### Normal profiles
- [TextureResource.Format.NormalEncoding.wy](./normalencoding/wy.md)
  A normal map with the X and Y components of a surface normal in the tangent space of the surface that RealityKit encodes in the alpha and green channels of a texture.
- [TextureResource.Format.NormalEncoding.xy](./normalencoding/xy.md)
  A normal map with the X and Y components of a surface normal in the tangent space of the surface that RealityKit encodes in the red and green channels of a texture.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Defining the format profile
- [TextureResource.Format.ColorSpace](./colorspace.md)
  A profile that specifies the interpretation of pixel values as a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format/normalencoding)*