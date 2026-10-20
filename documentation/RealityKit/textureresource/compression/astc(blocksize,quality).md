# astc(blockSize:quality:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Compresses the imported image with ASTC.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality = .fast) -> TextureResource.Compression
```

#### Discussion

If the device doesn’t support ASTC pixel formats, RealityKit applies compression as part of the `.reality` file export.

> **Note**: Remove an unused alpha channel from the source image to get better compression quality.

## See Also

### Specifying the compression settings
- [static var `default`: TextureResource.Compression](./default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](./none.md)
  A texture you can create with no compression.
- [TextureResource.Compression.ASTCBlockSize](./astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](./astcquality.md)
  Selects the level of processing time allocated to achieve compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression/astc(blocksize:quality:))*