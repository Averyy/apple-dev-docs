# MDLNoiseTexture

**Framework**: Model I/O  
**Kind**: class

A generator of texel data that creates a field of random noise.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLNoiseTexture
```

#### Overview

Like other procedural [`MDLTexture`](mdltexture.md) subclasses, the [`MDLNoiseTexture`](mdlnoisetexture.md) class generates texel data only when that data is first referenced, and then caches it for future use.

## Topics

### Creating a Noise Texture
- [init(scalarNoiseWithSmoothness: Float, name: String?, textureDimensions: vector_int2, channelCount: Int32, channelEncoding: MDLTextureChannelEncoding, grayscale: Bool)](mdlnoisetexture/init(scalarnoisewithsmoothness:name:texturedimensions:channelcount:channelencoding:grayscale:).md)
  Initializes a noise texture that creates random color noise.
- [init(vectorNoiseWithSmoothness: Float, name: String?, textureDimensions: vector_int2, channelEncoding: MDLTextureChannelEncoding)](mdlnoisetexture/init(vectornoisewithsmoothness:name:texturedimensions:channelencoding:).md)
  Initializes a noise texture that creates random directional noise.
### Initializers
- [init(cellularNoiseWithFrequency: Float, name: String?, textureDimensions: vector_int2, channelEncoding: MDLTextureChannelEncoding)](mdlnoisetexture/init(cellularnoisewithfrequency:name:texturedimensions:channelencoding:).md)

## Relationships

### Inherits From
- [MDLTexture](mdltexture.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLTexture](mdltexture.md)
  A source of texel data to be used in rendering material surface appearances.
- [class MDLCheckerboardTexture](mdlcheckerboardtexture.md)
  A generator of texel data that creates a checkerboard pattern with two specified colors.
- [class MDLColorSwatchTexture](mdlcolorswatchtexture.md)
  A generator of texel data that creates a gradient between two specified colors.
- [class MDLNormalMapTexture](mdlnormalmaptexture.md)
  A generator of texel data that computes a normal map from a supplied texture.
- [class MDLSkyCubeTexture](mdlskycubetexture.md)
  A generator of texel data that creates cube textures using a physically realistic simulation of the sunlit sky.
- [class MDLURLTexture](mdlurltexture.md)
  A lightweight reference to a URL from which to load texture data.
- [class MDLTextureFilter](mdltexturefilter.md)
  A description of filtering modes for a renderer to use when sampling from a texture.
- [class MDLTextureSampler](mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnoisetexture)*