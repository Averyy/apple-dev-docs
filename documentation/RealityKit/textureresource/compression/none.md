# none

**Framework**: RealityKit  
**Kind**: property

A texture you can create with no compression.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static var none: TextureResource.Compression { get }
```

#### Discussion

If you export this to a `.reality` file using [`write(to:)`](entity/write(to:).md), the texture remains uncompressed.

## See Also

- [static var `default`: TextureResource.Compression](textureresource/compression/default.md)
  A texture you can create and export with lossy compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](textureresource/compression/astc(blocksize:quality:).md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCBlockSize](textureresource/compression/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](textureresource/compression/astcquality.md)
  Selects the level of processing time allocated to achieve compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression/none)*