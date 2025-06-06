# mipLevelCount

**Framework**: Model I/O  
**Kind**: property

The number of mipmap levels contained in the texture image data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var mipLevelCount: Int { get }
```

#### Discussion

Mipmapping is a technique that uses multiple sizes of a texture image to increase rendering performance. If this property’s value is zero, the texture contains a single image, whose size matches the [`dimensions`](mdltexture/dimensions.md) property. If this value is 1, the texture contains an additional image at half the original dimensions; if this value is 2, the texture contains images at the original size, at half size, and at quarter size; and so on.

## See Also

- [var dimensions: vector_int2](mdltexture/dimensions.md)
  The width and height, in texels, of the texture image.
- [var rowStride: Int](mdltexture/rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelCount: Int](mdltexture/channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](mdltexture/iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/miplevelcount)*