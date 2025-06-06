# dimensions

**Framework**: Model I/O  
**Kind**: property

The width and height, in texels, of the texture image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dimensions: vector_int2 { get }
```

#### Discussion

If the texture contains multiple mipmap levels (the [`mipLevelCount`](mdltexture/miplevelcount.md) value is greater than zero), this property reflects the base (largest) mipmap level.

If the texture is a cube texture (the [`isCube`](mdltexture/iscube.md) value is [`true`](https://developer.apple.com/documentation/swift/true)), this property reflects the vertical arrangement of cube faces in the texture image data. That is, the texture’s height is six times its width, and the data represents six square images for the six sides of the cube.

## See Also

- [var rowStride: Int](mdltexture/rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelCount: Int](mdltexture/channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](mdltexture/iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.
- [var mipLevelCount: Int](mdltexture/miplevelcount.md)
  The number of mipmap levels contained in the texture image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/dimensions)*