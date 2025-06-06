# init(scalarNoiseWithSmoothness:name:textureDimensions:channelCount:channelEncoding:grayscale:)

**Framework**: Model I/O  
**Kind**: init

Initializes a noise texture that creates random color noise.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(scalarNoiseWithSmoothness smoothness: Float, name: String?, textureDimensions: vector_int2, channelCount: Int32, channelEncoding: MDLTextureChannelEncoding, grayscale: Bool)
```

#### Return Value

A new color noise texture object.

#### Discussion

A color noise texture has random values for each color channel and can be tiled or mirrored without showing visible borders.

This initializer does not generate texel data; the [`MDLNoiseTexture`](mdlnoisetexture.md) class automatically generates data and caches it for reuse when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data.

## Parameters

- `smoothness`: A value that indicates how similar neighboring texels will be in the resulting texture. The value should be between   and  . A value of   generates a smooth surface.
- `name`: The   property for the new texture object.
- `textureDimensions`: The texel dimensions (width and height) of the texture image.
- `channelCount`: The number of channels per texel—for example, 1 for a grayscale texture, 3 for an RGB color texture, or 4 for RGBA.
- `channelEncoding`: The data format for each channel value per texel—for example, 8-bit integer or 32-bit floating point. For possible values, see  .
- `grayscale`: If  , all four components of each texel will have equal values. If  , all four values are completely randomized.

## See Also

- [init(vectorNoiseWithSmoothness: Float, name: String?, textureDimensions: vector_int2, channelEncoding: MDLTextureChannelEncoding)](mdlnoisetexture/init(vectornoisewithsmoothness:name:texturedimensions:channelencoding:).md)
  Initializes a noise texture that creates random directional noise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnoisetexture/init(scalarnoisewithsmoothness:name:texturedimensions:channelcount:channelencoding:grayscale:))*