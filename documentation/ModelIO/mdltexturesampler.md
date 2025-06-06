# MDLTextureSampler

**Framework**: Model I/O  
**Kind**: class

An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLTextureSampler
```

#### Overview

You use texture samplers as material property values with the [`MDLMaterialProperty`](mdlmaterialproperty.md) class.

## Topics

### Working with Texture Parameters
- [var texture: MDLTexture?](mdltexturesampler/texture.md)
  The texture object that provides image data for sampling.
- [var hardwareFilter: MDLTextureFilter?](mdltexturesampler/hardwarefilter.md)
  An object that describes filtering modes for sampling from the texture.
- [var transform: MDLTransform?](mdltexturesampler/transform.md)
  The transformation to be applied to texture coordinate data before sampling from the texture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLTexture](mdltexture.md)
  A source of texel data to be used in rendering material surface appearances.
- [class MDLCheckerboardTexture](mdlcheckerboardtexture.md)
  A generator of texel data that creates a checkerboard pattern with two specified colors.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturesampler)*