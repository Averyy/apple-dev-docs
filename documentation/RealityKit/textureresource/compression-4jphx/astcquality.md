# TextureResource.Compression.ASTCQuality

**Framework**: RealityKit  
**Kind**: enum

Selects the level of processing time allocated to achieve compression.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
enum ASTCQuality
```

#### Overview

> ❗ **Important**: Given its processing cost, runtime compression isn’t recommended for interactive apps, as opposed to loading `.reality` files or `.ktx` precompressed textures. Higher quality levels are recommended for pipelines assembling scenes you intend to export to `.reality` files.

## Topics

### Enumeration Cases
- [TextureResource.Compression.ASTCQuality.exhaustive](textureresource/compression-4jphx/astcquality/exhaustive.md)
  Compresses optimally, achieving minor gains over high-level compression at the cost of much longer processing times.
- [TextureResource.Compression.ASTCQuality.fast](textureresource/compression-4jphx/astcquality/fast.md)
  Compresses as fast as possible.
- [TextureResource.Compression.ASTCQuality.high](textureresource/compression-4jphx/astcquality/high.md)
  Compresses with a focus on quality, reaching close to optimal quality while still spending much less time than exhaustive-level compression.
- [TextureResource.Compression.ASTCQuality.normal](textureresource/compression-4jphx/astcquality/normal.md)
  Compresses with a good balance between quality and processing time.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/compression-4jphx/astcquality)*