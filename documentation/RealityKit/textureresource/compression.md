# TextureResource.Compression

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The compression to apply when importing an image as a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Compression
```

## Overview

Compression allows varying levels of memory usage gains at the cost of image-quality reduction.

## Topics

### Specifying the compression settings
- [static var `default`: TextureResource.Compression](./compression/default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](./compression/none.md)
  A texture you can create with no compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](./compression/astc%28blocksize,quality%29.md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCBlockSize](./compression/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](./compression/astcquality.md)
  Selects the level of processing time allocated to achieve compression.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a texture resource
- [TextureResource.Contents](./contents.md)
  An object that references the pixel data for each mipmap level of a texture.
- [TextureResource.Format](./format.md)
  The pixel format and encoding of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression)*