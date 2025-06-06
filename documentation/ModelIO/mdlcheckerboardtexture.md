# MDLCheckerboardTexture

**Framework**: Model I/O  
**Kind**: class

A generator of texel data that creates a checkerboard pattern with two specified colors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLCheckerboardTexture
```

#### Overview

Like other procedural [`MDLTexture`](mdltexture.md) subclasses, the [`MDLCheckerboardTexture`](mdlcheckerboardtexture.md) class generates texel data only when that data is first referenced, and then caches it for future use.

## Topics

### Creating a Checkerboard Texture
- [init(divisions: Float, name: String?, dimensions: vector_int2, channelCount: Int32, channelEncoding: MDLTextureChannelEncoding, color1: CGColor, color2: CGColor)](mdlcheckerboardtexture/init(divisions:name:dimensions:channelcount:channelencoding:color1:color2:).md)
  Initializes a checkerboard texture with the specified colors and other properties.
### Configuring the Checkerboard Pattern
- [var color1: CGColor?](mdlcheckerboardtexture/color1.md)
  The color for half of the squares in the checkerboard pattern.
- [var color2: CGColor?](mdlcheckerboardtexture/color2.md)
  The color for the other half of the squares in the checkerboard pattern.
- [var divisions: Float](mdlcheckerboardtexture/divisions.md)
  The number of squares along each dimension in the checkerboard pattern.

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
- [class MDLColorSwatchTexture](mdlcolorswatchtexture.md)
  A generator of texel data that creates a gradient between two specified colors.
- [class MDLNoiseTexture](mdlnoisetexture.md)
  A generator of texel data that creates a field of random noise.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcheckerboardtexture)*