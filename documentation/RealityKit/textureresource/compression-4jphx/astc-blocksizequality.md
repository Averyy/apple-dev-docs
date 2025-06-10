# astc(blockSize:quality:)

**Framework**: RealityKit  
**Kind**: method

Compresses the imported image with ASTC.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality = .fast) -> TextureResource.Compression
```

#### Discussion

If the device doesn’t support ASTC pixel formats, RealityKit applies compression as part of the `.reality` file export.

> **Note**: Remove an unused alpha channel from the source image to get better compression quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression-4jphx/astc(blocksize:quality:))*