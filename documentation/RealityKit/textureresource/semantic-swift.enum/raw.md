# TextureResource.Semantic.raw

**Framework**: RealityKit  
**Kind**: case

Use the texture unmodified.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case raw
```

#### Discussion

For texture properties that use the `raw` semantic, the number of channels and values is the same as the source image. If the source image contains color space information, RealityKit ignores it. For `raw` textures, each individual pixel contains one floating-point value between `0.0` and `1.0` for each channel in the source image. For example, a grayscale source image results in a texture that contains one value per pixel, and an RGB source image results in three values per pixel.

## See Also

- [TextureResource.Semantic.color](textureresource/semantic-swift.enum/color.md)
  Use the texture to store colors data.
- [TextureResource.Semantic.hdrColor](textureresource/semantic-swift.enum/hdrcolor.md)
  Use the texture to store a high-dynamic range image.
- [TextureResource.Semantic.normal](textureresource/semantic-swift.enum/normal.md)
  Use the texture to store surface normals.
- [TextureResource.Semantic.scalar](textureresource/semantic-swift.enum/scalar.md)
  Use the texture to store a single value in each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/semantic-swift.enum/raw)*