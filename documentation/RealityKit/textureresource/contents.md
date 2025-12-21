# TextureResource.Contents

**Framework**: RealityKit  
**Kind**: struct

An object that references the pixel data for each mipmap level of a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Contents
```

#### Overview

Mipmaps are progressively smaller versions of the same texture image. Each level is half the size of the previous level, with a minimum size of 1 pixel in each dimension.

## Topics

### Creating the content
- [init(mipmapLevels: [TextureResource.Contents.MipmapLevel])](textureresource/contents/init(mipmaplevels:).md)
  Creates a texture contents object from an array of mipmaps.
### Defining the content
- [TextureResource.Contents.MipmapLevel](textureresource/contents/mipmaplevel.md)
  An object that references the pixel data for a single mipmap of a texture.
- [TextureResource.Contents.Slice](textureresource/contents/slice.md)
  An object that references the pixel data for a single slice of a mipmap.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TextureResource.Format](textureresource/format.md)
  The pixel format and encoding of a texture.
- [TextureResource.Compression](textureresource/compression.md)
  The compression to apply when importing an image as a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/contents)*