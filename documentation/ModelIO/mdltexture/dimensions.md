# dimensions

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) vector_int2 dimensions;
```

## Discussion

If the texture contains multiple mipmap levels (the [`mipLevelCount`](./miplevelcount.md) value is greater than zero), this property reflects the base (largest) mipmap level.

If the texture is a cube texture (the [`isCube`](./iscube.md) value is [`true`](../../Swift/true.md)), this property reflects the vertical arrangement of cube faces in the texture image data. That is, the texture’s height is six times its width, and the data represents six square images for the six sides of the cube.

## See Also

### Examining Texture Attributes
- [var rowStride: Int](./rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelCount: Int](./channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](./channelencoding.md)
  The data format for each channel value per texel.
- [var isCube: Bool](./iscube.md)
  A Boolean value that indicates whether the texture is a cube textures.
- [var mipLevelCount: Int](./miplevelcount.md)
  The number of mipmap levels contained in the texture image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/dimensions)*