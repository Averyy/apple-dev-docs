# GLKEffectPropertyTexture

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

Texture drawing parameters for use in GLKit rendering effects.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKEffectPropertyTexture
```

```objc
@interface GLKEffectPropertyTexture : GLKEffectProperty
```

#### Overview

The [`GLKEffectPropertyTexture`](./glkeffectpropertytexture.md) class defines properties that are used to configure an OpenGL texturing operation. The texturing operation combines an input color and a color sampled from the texture and outputs a new color to the next stage of calculations. The [`envMode`](./glkeffectpropertytexture/envmode.md) property determines the function used to calculate the output color from the two input colors.

If an effect only includes a single texture property, then the input color is the lighting color calculated by the lighting stage of the graphics pipeline. An effect can also include multiple [`GLKEffectPropertyTexture`](./glkeffectpropertytexture.md) objects. When an effect includes multiple properties, the first texture stage uses the lighting color as the first input color. Each texture stage after that uses the output of the previous stage as the input color.

## Topics

### Configuring Texture Properties
- [var enabled: GLboolean](./glkeffectpropertytexture/enabled.md)
  A Boolean value that indicates whether this texture is used to texture drawn primitives.
- [var envMode: GLKTextureEnvMode](./glkeffectpropertytexture/envmode.md)
  The mode the texture uses to compute its output fragment color. See [`GLKTextureEnvMode`](./glktextureenvmode.md).
- [var name: GLuint](./glkeffectpropertytexture/name.md)
  The OpenGL name for the texture being sampled by this texture stage.
- [var target: GLKTextureTarget](./glkeffectpropertytexture/target.md)
  The kind of texture pointed to by the texture stage. See [`GLKTextureTarget`](./glktexturetarget.md).
### Constants
- [enum GLKTextureTarget](./glktexturetarget.md)
  The kind of texture pointed to by the property.
- [enum GLKTextureEnvMode](./glktextureenvmode.md)
  The mode used to combine the texture with other color components.

## Relationships

### Inherits From
- [GLKEffectProperty](./glkeffectproperty.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Rendering Effect Parameters
- [class GLKEffectProperty](./glkeffectproperty.md)
  The abstract superclass for configuration information used in GLKit rendering effects.
- [class GLKEffectPropertyFog](./glkeffectpropertyfog.md)
  Fog drawing information for use in GLKit rendering effects.
- [class GLKEffectPropertyLight](./glkeffectpropertylight.md)
  Lighting information for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](./glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](./glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](./glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture)*