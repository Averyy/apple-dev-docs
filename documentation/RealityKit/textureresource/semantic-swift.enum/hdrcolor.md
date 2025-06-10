# TextureResource.Semantic.hdrColor

**Framework**: RealityKit  
**Kind**: case

Use the texture to store a high-dynamic range image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case hdrColor
```

#### Discussion

Properties that specify a semantic of `hdrColor` use the texture to store high-dynamic range RGB color data. If the source image contains color space information, RealityKit modifies the individual pixels to fit the color space. If the source image is grayscale, RealityKit converts it to an RGB image first.

## See Also

- [TextureResource.Semantic.raw](textureresource/semantic-swift.enum/raw.md)
  Use the texture unmodified.
- [TextureResource.Semantic.color](textureresource/semantic-swift.enum/color.md)
  Use the texture to store colors data.
- [TextureResource.Semantic.normal](textureresource/semantic-swift.enum/normal.md)
  Use the texture to store surface normals.
- [TextureResource.Semantic.scalar](textureresource/semantic-swift.enum/scalar.md)
  Use the texture to store a single value in each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/semantic-swift.enum/hdrcolor)*