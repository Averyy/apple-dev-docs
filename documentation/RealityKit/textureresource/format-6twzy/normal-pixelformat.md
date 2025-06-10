# normal(_:pixelFormat:)

**Framework**: RealityKit  
**Kind**: method

Indicates that a texture is a normal map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static func normal(_ encoding: TextureResource.Format.NormalEncoding, pixelFormat: MTLPixelFormat) -> TextureResource.Format
```

#### Discussion

The created texture uses the [`TextureResource.Semantic.normal`](textureresource/semantic-swift.enum/normal.md) semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format-6twzy/normal(_:pixelformat:))*