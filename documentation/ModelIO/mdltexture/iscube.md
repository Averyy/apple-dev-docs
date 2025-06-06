# isCube

**Framework**: Model I/O  
**Kind**: property

A Boolean value that indicates whether the texture is a cube textures.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isCube: Bool { get set }
```

#### Discussion

Cube textures are used in skybox rendering, light probes, and environment maps. If this property’s value is [`true`](https://developer.apple.com/documentation/swift/true), the texture object represents a cube texture. In this case, the texture’s image data (accessible with the methods in Accessing Texture Data) contains six square images arranged vertically. The images represent the +X, -X, +Y, -Y, +Z, and -Z faces of the cube (in that order), and the [`dimensions`](mdltexture/dimensions.md) property reflects this arrangement (height is six times width).

## See Also

- [var dimensions: vector_int2](mdltexture/dimensions.md)
  The width and height, in texels, of the texture image.
- [var rowStride: Int](mdltexture/rowstride.md)
  The number of bytes between the first texel in a row of image data and the first texel in the next row.
- [var channelCount: Int](mdltexture/channelcount.md)
  The number of channels per texel.
- [var channelEncoding: MDLTextureChannelEncoding](mdltexture/channelencoding.md)
  The data format for each channel value per texel.
- [var mipLevelCount: Int](mdltexture/miplevelcount.md)
  The number of mipmap levels contained in the texture image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/iscube)*