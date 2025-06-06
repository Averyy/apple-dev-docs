# TextureResource.Format

**Framework**: RealityKit  
**Kind**: struct

The pixel format and encoding of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Format
```

#### Overview

The texture’s format controls the sampling and conversions (if any) to use when rendering with that texture.

## Topics

### Creating the format
- [static func color(TextureResource.Format.ColorSpace, pixelFormat: MTLPixelFormat) -> TextureResource.Format](textureresource/format/color(_:pixelformat:).md)
  Indicates that a texture contains color data to interpret in a specific color space.
- [static func normal(TextureResource.Format.NormalEncoding, pixelFormat: MTLPixelFormat) -> TextureResource.Format](textureresource/format/normal(_:pixelformat:).md)
  Indicates that a texture is a normal map.
- [static func raw(pixelFormat: MTLPixelFormat) -> TextureResource.Format](textureresource/format/raw(pixelformat:).md)
  Indicates a texture for unmodified use by a shader.
### Defining the format profile
- [TextureResource.Format.ColorSpace](textureresource/format/colorspace.md)
  A profile that specifies the interpretation of pixel values as a color.
- [TextureResource.Format.NormalEncoding](textureresource/format/normalencoding.md)
  A profile that specifies the interpretation of pixel values as a normal.
### Default Implementations
- [Equatable Implementations](textureresource/format/equatable-implementations.md)
- [Hashable Implementations](textureresource/format/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(from: LowLevelTexture) throws](textureresource/init(from:)-3psmc.md)
  Synchronously creates a texture resource from a low-level texture.
- [convenience init(from: LowLevelTexture) async throws](textureresource/init(from:)-42r55.md)
  Asynchronously creates a texture resource from a low-level texture.
- [TextureResource.Contents](textureresource/contents.md)
  An object that references the pixel data for each mipmap level of a texture.
- [TextureResource.Compression](textureresource/compression.md)
  The compression to apply when importing an image as a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format)*