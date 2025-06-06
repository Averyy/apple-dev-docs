# MDLURLTexture

**Framework**: Model I/O  
**Kind**: class

A lightweight reference to a URL from which to load texture data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLURLTexture
```

#### Overview

Unlike the superclass [`MDLTexture`](mdltexture.md), the [`MDLURLTexture`](mdlurltexture.md) class loads texel data from the file at that URL only when that data is first referenced, and then caches it for future use.

## Topics

### Creating a URL Texture
- [init(url: URL, name: String?)](mdlurltexture/init(url:name:).md)
  Initializes a texture that loads its texel data from a file at the specified URL.
### Inspecting the Texture URL
- [var url: URL](mdlurltexture/url.md)
  The URL from which to load texture data.

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
- [class MDLNoiseTexture](mdlnoisetexture.md)
  A generator of texel data that creates a field of random noise.
- [class MDLNormalMapTexture](mdlnormalmaptexture.md)
  A generator of texel data that computes a normal map from a supplied texture.
- [class MDLSkyCubeTexture](mdlskycubetexture.md)
  A generator of texel data that creates cube textures using a physically realistic simulation of the sunlit sky.
- [class MDLTextureFilter](mdltexturefilter.md)
  A description of filtering modes for a renderer to use when sampling from a texture.
- [class MDLTextureSampler](mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlurltexture)*