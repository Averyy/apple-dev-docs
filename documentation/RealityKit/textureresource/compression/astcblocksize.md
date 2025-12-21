# TextureResource.Compression.ASTCBlockSize

**Framework**: RealityKit  
**Kind**: enum

The compressed block size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
enum ASTCBlockSize
```

#### Overview

> **Note**: RealityKit stores block pixel data in groups of 128 bits. For instance, a `block4x4` bits per pixel is 128/(4*4) = 8 bit per pixel.

## Topics

### Compression block sizes
- [TextureResource.Compression.ASTCBlockSize.block4x4](textureresource/compression/astcblocksize/block4x4.md)
- [TextureResource.Compression.ASTCBlockSize.block5x4](textureresource/compression/astcblocksize/block5x4.md)
- [TextureResource.Compression.ASTCBlockSize.block5x5](textureresource/compression/astcblocksize/block5x5.md)
- [TextureResource.Compression.ASTCBlockSize.block6x5](textureresource/compression/astcblocksize/block6x5.md)
- [TextureResource.Compression.ASTCBlockSize.block6x6](textureresource/compression/astcblocksize/block6x6.md)
- [TextureResource.Compression.ASTCBlockSize.block8x5](textureresource/compression/astcblocksize/block8x5.md)
- [TextureResource.Compression.ASTCBlockSize.block8x6](textureresource/compression/astcblocksize/block8x6.md)
- [TextureResource.Compression.ASTCBlockSize.block8x8](textureresource/compression/astcblocksize/block8x8.md)
- [TextureResource.Compression.ASTCBlockSize.block10x10](textureresource/compression/astcblocksize/block10x10.md)
- [TextureResource.Compression.ASTCBlockSize.block10x5](textureresource/compression/astcblocksize/block10x5.md)
- [TextureResource.Compression.ASTCBlockSize.block10x6](textureresource/compression/astcblocksize/block10x6.md)
- [TextureResource.Compression.ASTCBlockSize.block10x8](textureresource/compression/astcblocksize/block10x8.md)
- [TextureResource.Compression.ASTCBlockSize.block12x10](textureresource/compression/astcblocksize/block12x10.md)
- [TextureResource.Compression.ASTCBlockSize.block12x12](textureresource/compression/astcblocksize/block12x12.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var `default`: TextureResource.Compression](textureresource/compression/default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](textureresource/compression/none.md)
  A texture you can create with no compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](textureresource/compression/astc(blocksize:quality:).md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCQuality](textureresource/compression/astcquality.md)
  Selects the level of processing time allocated to achieve compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression/astcblocksize)*