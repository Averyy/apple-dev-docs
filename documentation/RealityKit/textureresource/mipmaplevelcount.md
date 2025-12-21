# mipmapLevelCount

**Framework**: RealityKit  
**Kind**: property

The number of mipmaps for the texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var mipmapLevelCount: Int { get }
```

#### Discussion

Mipmaps are additional copies of the same texture at different resolutions. This property contains the number of different versions of the texture, including the original-size version.

## See Also

- [var textureType: MTLTextureType](textureresource/texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](textureresource/pixelformat.md)
  The texture’s pixel format.
- [var height: Int](textureresource/height.md)
  The height of the texture image, in pixels.
- [var width: Int](textureresource/width.md)
  The width of the texture image, in pixels.
- [var depth: Int](textureresource/depth.md)
  The depth of the texture image, in pixels.
- [var arrayLength: Int](textureresource/arraylength.md)
  The number of slices in the texture array.
- [var semantic: TextureResource.Semantic?](textureresource/semantic-swift.property.md)
  The intended usage of the texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/mipmaplevelcount)*