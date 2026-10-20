# TextureResource.Format

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The pixel format and encoding of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Format
```

#### Overview

The texture’s format controls the sampling and conversions (if any) to use when rendering with that texture.

## Topics

### Creating the format
- [static func color(TextureResource.Format.ColorSpace, pixelFormat: MTLPixelFormat) -> TextureResource.Format](./format/color%28_,pixelformat%29.md)
  Indicates that a texture contains color data to interpret in a specific color space.
- [static func normal(TextureResource.Format.NormalEncoding, pixelFormat: MTLPixelFormat) -> TextureResource.Format](./format/normal%28_,pixelformat%29.md)
  Indicates that a texture is a normal map.
- [static func raw(pixelFormat: MTLPixelFormat) -> TextureResource.Format](./format/raw%28pixelformat%29.md)
  Indicates a texture for unmodified use by a shader.
### Defining the format profile
- [TextureResource.Format.ColorSpace](./format/colorspace.md)
  A profile that specifies the interpretation of pixel values as a color.
- [TextureResource.Format.NormalEncoding](./format/normalencoding.md)
  A profile that specifies the interpretation of pixel values as a normal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a texture resource
- [TextureResource.Contents](./contents.md)
  An object that references the pixel data for each mipmap level of a texture.
- [TextureResource.Compression](./compression.md)
  The compression to apply when importing an image as a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format)*