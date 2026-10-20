# MDLNormalMapTexture

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

A generator of texel data that computes a normal map from a supplied texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLNormalMapTexture
```

```objc
@interface MDLNormalMapTexture : MDLTexture
```

#### Overview

This class examines the shapes of contrasting areas in an input texture to generate a normal map that produces an embossed appearance when rendered with lighting. The figure below shows the normal map generated from an example texture and the effect of using this normal map with lighting in a typical renderer.

![](https://developer.apple.com/tutorials/images/com.apple.modelio/media-1965618@2x.png)

Like other procedural [`MDLTexture`](./mdltexture.md) subclasses, the [`MDLNormalMapTexture`](./mdlnormalmaptexture.md) class generates texel data only when that data is first referenced, and caches it for future use.

## Topics

### Creating a Normal Map Texture
- [init(byGeneratingNormalMapWith: MDLTexture, name: String?, smoothness: Float, contrast: Float)](./mdlnormalmaptexture/init%28bygeneratingnormalmapwith,name,smoothness,contrast%29.md)
  Initializes a normal map to be generated from the specified texture.
### Initializers
- [init(byGeneratingNormalMapWithTexture: MDLTexture, name: String?, smoothness: Float, contrast: Float)](./mdlnormalmaptexture/init%28bygeneratingnormalmapwithtexture,name,smoothness,contrast%29.md)

## Relationships

### Inherits From
- [MDLTexture](./mdltexture.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MDLNamed](./mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Textures
- [class MDLTexture](./mdltexture.md)
  A source of texel data to be used in rendering material surface appearances.
- [class MDLCheckerboardTexture](./mdlcheckerboardtexture.md)
  A generator of texel data that creates a checkerboard pattern with two specified colors.
- [class MDLColorSwatchTexture](./mdlcolorswatchtexture.md)
  A generator of texel data that creates a gradient between two specified colors.
- [class MDLNoiseTexture](./mdlnoisetexture.md)
  A generator of texel data that creates a field of random noise.
- [class MDLSkyCubeTexture](./mdlskycubetexture.md)
  A generator of texel data that creates cube textures using a physically realistic simulation of the sunlit sky.
- [class MDLURLTexture](./mdlurltexture.md)
  A lightweight reference to a URL from which to load texture data.
- [class MDLTextureFilter](./mdltexturefilter.md)
  A description of filtering modes for a renderer to use when sampling from a texture.
- [class MDLTextureSampler](./mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture)*