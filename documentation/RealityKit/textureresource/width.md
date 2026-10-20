# width

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The width of the texture image, in pixels.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var width: Int { get }
```

## See Also

### Describing the texture
- [var textureType: MTLTextureType](./texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The texture’s pixel format.
- [var height: Int](./height.md)
  The height of the texture image, in pixels.
- [var depth: Int](./depth.md)
  The depth of the texture image, in pixels.
- [var arrayLength: Int](./arraylength.md)
  The number of slices in the texture array.
- [var mipmapLevelCount: Int](./mipmaplevelcount.md)
  The number of mipmaps for the texture.
- [var semantic: TextureResource.Semantic?](./semantic-swift.property.md)
  The intended usage of the texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/width)*