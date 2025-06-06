# TextureResource.Compression

**Framework**: RealityKit  
**Kind**: struct

The compression to apply when importing an image as a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Compression
```

#### Overview

Compression allows varying levels of memory usage gains at the cost of image-quality reduction.

## Topics

### Specifying the compression settings
- [static var `default`: TextureResource.Compression](textureresource/compression/default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](textureresource/compression/none.md)
  A texture you can create with no compression.
- [static func astc(blockSize: TextureResource.Compression.ASTCBlockSize, quality: TextureResource.Compression.ASTCQuality) -> TextureResource.Compression](textureresource/compression/astc(blocksize:quality:).md)
  Compresses the imported image with ASTC.
- [TextureResource.Compression.ASTCBlockSize](textureresource/compression/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](textureresource/compression/astcquality.md)
  Selects the level of processing time allocated to achieve compression.
### Comparing compression settings
- [func hash(into: inout Hasher)](textureresource/compression/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](textureresource/compression/hashvalue.md)
  The hash value.
### Operators
- [static func == (TextureResource.Compression, TextureResource.Compression) -> Bool](textureresource/compression/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](textureresource/compression/equatable-implementations.md)

## Relationships

### Conforms To
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
- [TextureResource.Format](textureresource/format.md)
  The pixel format and encoding of a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression)*