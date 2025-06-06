# textureType

**Framework**: RealityKit  
**Kind**: property

The dimension and arrangement of the texture image data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var textureType: MTLTextureType { get }
```

## See Also

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
- [var mipmapLevelCount: Int](textureresource/mipmaplevelcount.md)
  The number of mipmaps for the texture.
- [var semantic: TextureResource.Semantic?](textureresource/semantic-swift.property.md)
  The intended usage of the texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/texturetype)*