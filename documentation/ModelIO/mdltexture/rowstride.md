# rowStride

**Framework**: Model I/O  
**Kind**: property

The number of bytes between the first texel in a row of image data and the first texel in the next row.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rowStride: Int { get }
```

#### Discussion

If this value is zero, the texture does not support direct addressing of texels—this is the case for some compressed texture formats.

## See Also

- [var dimensions: vector_int2](mdltexture/dimensions.md)
  The width and height, in texels, of the texture image.
- [var channelCount: Int](mdltexture/channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](mdltexture/iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.
- [var mipLevelCount: Int](mdltexture/miplevelcount.md)
  The number of mipmap levels contained in the texture image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/rowstride)*