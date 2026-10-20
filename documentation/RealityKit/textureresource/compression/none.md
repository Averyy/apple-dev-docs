# none

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

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

If you export this to a `.reality` file using [`write(to:)`](../../entity/write%28to%29.md), the texture remains uncompressed.

## See Also

### Specifying the compression settings
- [static var `default`: TextureResource.Compression](./default.md)
  A texture you can create and export with lossy compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](./astc%28blocksize,quality%29.md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCBlockSize](./astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](./astcquality.md)
  Selects the level of processing time allocated to achieve compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression/none)*