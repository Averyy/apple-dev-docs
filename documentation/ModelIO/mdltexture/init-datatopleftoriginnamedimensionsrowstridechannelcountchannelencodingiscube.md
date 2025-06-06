# init(data:topLeftOrigin:name:dimensions:rowStride:channelCount:channelEncoding:isCube:)

**Framework**: Model I/O  
**Kind**: init

Initializes a texture object with the specified image data and properties.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(data pixelData: Data?, topLeftOrigin: Bool, name: String?, dimensions: vector_int2, rowStride: Int, channelCount: Int, channelEncoding: MDLTextureChannelEncoding, isCube: Bool)
```

#### Return Value

A new texture object.

## Parameters

- `pixelData`: The texture image data. Pass   for subclasses of   that create their own texture data.
- `topLeftOrigin`: If  , the image data is organized such that its first pixel represents the top left corner of the image. If  , the first pixel represents the bottom left corner of the image.
- `name`: A descriptive name for the texture. Use the   property to reference this name after initialization.
- `dimensions`: The texel dimensions (width and height) of the texture image.
- `rowStride`: The number of bytes between the first texel in a row of image data and the first texel in the next row. If zero, the texture does not support direct addressing of texels—this is the case for some compressed texture formats.
- `channelCount`: The number of channels per texel—for example, 1 for a grayscale texture, 3 for an RGB color texture, or 4 for RGBA.
- `channelEncoding`: The data format for each channel value per texel—for example, 8-bit integer or 32-bit floating point. For possible values, see  .
- `isCube`: If  , the image data represents an arrangement of six square images, each of which is a face for a cube texture. If  , the texture is a single 2D image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/init(data:topleftorigin:name:dimensions:rowstride:channelcount:channelencoding:iscube:))*