# raw(pixelFormat:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Indicates a texture for unmodified use by a shader.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static func raw(pixelFormat: MTLPixelFormat) -> TextureResource.Format
```

## Discussion

The created texture uses the [`TextureResource.Semantic.raw`](../semantic-swift.enum/raw.md) semantic.

## See Also

### Creating the format
- [static func color(TextureResource.Format.ColorSpace, pixelFormat: MTLPixelFormat) -> TextureResource.Format](./color%28_,pixelformat%29.md)
  Indicates that a texture contains color data to interpret in a specific color space.
- [static func normal(TextureResource.Format.NormalEncoding, pixelFormat: MTLPixelFormat) -> TextureResource.Format](./normal%28_,pixelformat%29.md)
  Indicates that a texture is a normal map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/format/raw(pixelformat:))*