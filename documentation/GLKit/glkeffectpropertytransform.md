# GLKEffectPropertyTransform

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

Coordinate transform information for use in GLKit rendering effects.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKEffectPropertyTransform
```

```objc
@interface GLKEffectPropertyTransform : GLKEffectProperty
```

#### Overview

The [`GLKEffectPropertyTransform`](./glkeffectpropertytransform.md) class defines properties that provide the coordinate transformations to be performed when rendering the effect.

## Topics

### Configuring Modelview Properties
- [var modelviewMatrix: GLKMatrix4](./glkeffectpropertytransform/modelviewmatrix.md)
  The matrix used to transform position coordinates from world space to eye space.
- [var normalMatrix: GLKMatrix3](./glkeffectpropertytransform/normalmatrix.md)
  The matrix used to transform normal coordinates from world space to eye space.
### Configuring the Projection Matrix
- [var projectionMatrix: GLKMatrix4](./glkeffectpropertytransform/projectionmatrix.md)
  The matrix used to transform position coordinates from eye space to projection space.

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
- [class GLKEffectPropertyMaterial](./glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [GLKit Effects Constants](./glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform)*