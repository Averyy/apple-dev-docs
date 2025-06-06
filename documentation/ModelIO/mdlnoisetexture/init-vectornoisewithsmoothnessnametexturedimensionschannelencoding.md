# init(vectorNoiseWithSmoothness:name:textureDimensions:channelEncoding:)

**Framework**: Model I/O  
**Kind**: init

Initializes a noise texture that creates random directional noise.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(vectorNoiseWithSmoothness smoothness: Float, name: String?, textureDimensions: vector_int2, channelEncoding: MDLTextureChannelEncoding)
```

#### Return Value

A new directional noise texture object.

#### Discussion

Unlike a color noise texture, in which the RGBA channels are independently randomized, a directional noise texture treats each texel’s RGB channels together as the XYZ components of a random direction vector, and the A channel as a scalar for the vector’s direction.

This initializer does not generate texel data; the [`MDLNoiseTexture`](mdlnoisetexture.md) class automatically generates data and caches it for reuse when you use one of the [`MDLTexture`](mdltexture.md) methods listed in Accessing Texture Data.

## Parameters

- `smoothness`: A value that indicates how similar neighboring texels will be in the resulting texture. The value should be between   and  . A value of   generates a smooth surface.
- `name`: The   property for the new texture object.
- `textureDimensions`: The texel dimensions (width and height) of the texture image.
- `channelEncoding`: The data format for each channel value per texel—for example, 8-bit integer or 32-bit floating point. For possible values, see  .

## See Also

- [init(scalarNoiseWithSmoothness: Float, name: String?, textureDimensions: vector_int2, channelCount: Int32, channelEncoding: MDLTextureChannelEncoding, grayscale: Bool)](mdlnoisetexture/init(scalarnoisewithsmoothness:name:texturedimensions:channelcount:channelencoding:grayscale:).md)
  Initializes a noise texture that creates random color noise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnoisetexture/init(vectornoisewithsmoothness:name:texturedimensions:channelencoding:))*