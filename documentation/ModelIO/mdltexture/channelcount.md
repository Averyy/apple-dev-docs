# channelCount

**Framework**: Model I/O  
**Kind**: property

The number of channels per texel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var channelCount: Int { get }
```

#### Discussion

For example, a grayscale texture has one channel (brightness) per texel, and a color texture may have three (RGB) or four (RGBA) channels per texel.

## See Also

- [var dimensions: vector_int2](mdltexture/dimensions.md)
  The width and height, in texels, of the texture image.
- [var rowStride: Int](mdltexture/rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](mdltexture/iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.
- [var mipLevelCount: Int](mdltexture/miplevelcount.md)
  The number of mipmap levels contained in the texture image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/channelcount)*