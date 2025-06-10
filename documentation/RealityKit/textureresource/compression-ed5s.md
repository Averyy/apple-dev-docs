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
- [static var `default`: TextureResource.Compression](textureresource/compression-ed5s/default.md)
  A texture you can create and export with lossy compression.
- [static var none: TextureResource.Compression](textureresource/compression-ed5s/none.md)
  A texture you can create with no compression.
### Enumerations
- [TextureResource.Compression.ASTCBlockSize](textureresource/compression-ed5s/astcblocksize.md)
  The compressed block size.
- [TextureResource.Compression.ASTCQuality](textureresource/compression-ed5s/astcquality.md)
  Selects the level of processing time allocated to achieve compression.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression-ed5s)*