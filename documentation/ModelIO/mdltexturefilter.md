# MDLTextureFilter

**Framework**: Model I/O  
**Kind**: class

A description of filtering modes for a renderer to use when sampling from a texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLTextureFilter
```

#### Overview

A texture filter, together with a [`MDLTexture`](mdltexture.md) object and transform information, form a [`MDLTextureSampler`](mdltexturesampler.md) object, which describes a texture and its rendering parameters for use in rendering one aspect of a [`MDLMaterial`](mdlmaterial.md) object’s surface appearance.

## Topics

### Managing Texture Coordinate Wrap Modes
- [var sWrapMode: MDLMaterialTextureWrapMode](mdltexturefilter/swrapmode.md)
  The coordinate wrapping mode for texture t-coordinates.
- [var tWrapMode: MDLMaterialTextureWrapMode](mdltexturefilter/twrapmode.md)
  The coordinate wrapping mode for texture t-coordinates.
- [var rWrapMode: MDLMaterialTextureWrapMode](mdltexturefilter/rwrapmode.md)
  The coordinate wrapping mode for texture r-coordinates.
### Managing Texture Filter Modes
- [var minFilter: MDLMaterialTextureFilterMode](mdltexturefilter/minfilter.md)
  The filter mode for rendering textures at sizes smaller than that of the original image.
- [var magFilter: MDLMaterialTextureFilterMode](mdltexturefilter/magfilter.md)
  The filter mode for rendering textures at sizes larger than that of the original image.
- [var mipFilter: MDLMaterialMipMapFilterMode](mdltexturefilter/mipfilter.md)
  The filter mode for rendering textures using mipmapping.
### Constants
- [enum MDLMaterialTextureWrapMode](mdlmaterialtexturewrapmode.md)
  Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](mdltexturefilter/swrapmode.md), [`tWrapMode`](mdltexturefilter/twrapmode.md), and [`rWrapMode`](mdltexturefilter/rwrapmode.md) properties.
- [enum MDLMaterialTextureFilterMode](mdlmaterialtexturefiltermode.md)
  Modes for sampling textures at coordinates between texels, used by the [`minFilter`](mdltexturefilter/minfilter.md) and [`magFilter`](mdltexturefilter/magfilter.md) properties.
- [enum MDLMaterialMipMapFilterMode](mdlmaterialmipmapfiltermode.md)
  Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](mdltexturefilter/mipfilter.md) property.

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
- [class MDLTextureSampler](mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturefilter)*