# TextureResource.Semantic.normal

**Framework**: RealityKit  
**Kind**: case

Use the texture to store surface normals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case normal
```

#### Discussion

Properties that specify a semantic of `normal` use the texture to store tangent-space surface normal vectors for use in lighting calculations. Each pixel’s `R` channel stores the `X` value from the vector. The `G` channel stores the `Y` value from the vector, and the `B` channel stores the `Z` value from the vector. All values are between `-1.0` and `1.0`.

## See Also

- [TextureResource.Semantic.raw](textureresource/semantic-swift.enum/raw.md)
  Use the texture unmodified.
- [TextureResource.Semantic.color](textureresource/semantic-swift.enum/color.md)
  Use the texture to store colors data.
- [TextureResource.Semantic.hdrColor](textureresource/semantic-swift.enum/hdrcolor.md)
  Use the texture to store a high-dynamic range image.
- [TextureResource.Semantic.scalar](textureresource/semantic-swift.enum/scalar.md)
  Use the texture to store a single value in each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/semantic-swift.enum/normal)*