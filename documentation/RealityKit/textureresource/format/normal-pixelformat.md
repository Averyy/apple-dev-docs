# normal(_:pixelFormat:)

**Framework**: RealityKit  
**Kind**: method

Indicates that a texture is a normal map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static func normal(_ encoding: TextureResource.Format.NormalEncoding, pixelFormat: MTLPixelFormat) -> TextureResource.Format
```

#### Discussion

The created texture uses the [`TextureResource.Semantic.normal`](textureresource/semantic-swift.enum/normal.md) semantic.

## See Also

- [static func color(TextureResource.Format.ColorSpace, pixelFormat: MTLPixelFormat) -> TextureResource.Format](textureresource/format/color(_:pixelformat:).md)
  Indicates that a texture contains color data to interpret in a specific color space.
- [static func raw(pixelFormat: MTLPixelFormat) -> TextureResource.Format](textureresource/format/raw(pixelformat:).md)
  Indicates a texture for unmodified use by a shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format/normal(_:pixelformat:))*