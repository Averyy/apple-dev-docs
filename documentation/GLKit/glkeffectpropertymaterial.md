# GLKEffectPropertyMaterial

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

Surface appearance properties for use in GLKit rendering effects.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKEffectPropertyMaterial
```

```objc
@interface GLKEffectPropertyMaterial : GLKEffectProperty
```

#### Overview

The [`GLKEffectPropertyMaterial`](./glkeffectpropertymaterial.md) class defines properties used to configure the characteristics of the surface being lit. The material properties for an effect interact with light properties on the same effect to determine how that surface is lit within the scene. The behavior of this class matches the material properties and lighting calculations defined in the OpenGL ES 1.1 specification.

## Topics

### Material Properties
- [var ambientColor: GLKVector4](./glkeffectpropertymaterial/ambientcolor.md)
  The ambient color of the material.
- [var diffuseColor: GLKVector4](./glkeffectpropertymaterial/diffusecolor.md)
  The diffuse color of the material.
- [var emissiveColor: GLKVector4](./glkeffectpropertymaterial/emissivecolor.md)
  The emissive color of the material.
- [var shininess: GLfloat](./glkeffectpropertymaterial/shininess.md)
  The shininess of the material, used when calculating specular lighting effects.
- [var specularColor: GLKVector4](./glkeffectpropertymaterial/specularcolor.md)
  The specular color of the material.

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
- [class GLKEffectPropertyTexture](./glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](./glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](./glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial)*