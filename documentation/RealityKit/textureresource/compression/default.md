# default

**Framework**: RealityKit  
**Kind**: property

A texture you can create and export with lossy compression.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static var `default`: TextureResource.Compression { get }
```

#### Discussion

The selected compression preserves perceptual texture details (no aggressive compression).

## See Also

- [static var none: TextureResource.Compression](textureresource/compression/none.md)
  A texture you can create with no compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](textureresource/compression/astc(blocksize:quality:).md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCBlockSize](textureresource/compression/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](textureresource/compression/astcquality.md)
  Selects the level of processing time allocated to achieve compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression/default)*