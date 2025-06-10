# TextureResource.Compression

**Framework**: RealityKit  
**Kind**: struct

The compression to apply when importing an image as a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct Compression
```

#### Overview

Compression allows varying levels of memory usage gains at the cost of image-quality reduction.

## Topics

### Type Properties
- [static var `default`: TextureResource.Compression](textureresource/compression-4jphx/default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](textureresource/compression-4jphx/none.md)
  A texture you can create with no compression.
### Type Methods
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](textureresource/compression-4jphx/astc(blocksize:quality:).md)
  Compresses the imported image with ASTC.
### Enumerations
- [TextureResource.Compression.ASTCBlockSize](textureresource/compression-4jphx/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](textureresource/compression-4jphx/astcquality.md)
  Selects the level of processing time allocated to achieve compression.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression-4jphx)*