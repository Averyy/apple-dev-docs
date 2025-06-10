# raw(pixelFormat:)

**Framework**: RealityKit  
**Kind**: method

Indicates a texture for unmodified use by a shader.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static func raw(pixelFormat: MTLPixelFormat) -> TextureResource.Format
```

#### Discussion

The created texture uses the [`TextureResource.Semantic.raw`](textureresource/semantic-swift.enum/raw.md) semantic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format-6twzy/raw(pixelformat:))*