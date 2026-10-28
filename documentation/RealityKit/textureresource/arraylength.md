# arrayLength

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The number of slices in the texture array.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var arrayLength: Int { get }
```

## Discussion

The value is `0` if it isn’t a texture array.

## See Also

### Describing the texture
- [var textureType: MTLTextureType](./texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The texture’s pixel format.
- [var height: Int](./height.md)
  The height of the texture image, in pixels.
- [var width: Int](./width.md)
  The width of the texture image, in pixels.
- [var depth: Int](./depth.md)
  The depth of the texture image, in pixels.
- [var mipmapLevelCount: Int](./mipmaplevelcount.md)
  The number of mipmaps for the texture.
- [var semantic: TextureResource.Semantic?](./semantic-swift.property.md)
  The intended usage of the texture resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/arraylength)*