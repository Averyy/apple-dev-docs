# GLKEffectPropertyFog

**Framework**: GLKit  
**Kind**: class

Fog drawing information for use in GLKit rendering effects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKEffectPropertyFog
```

#### Overview

These properties are specifically designed to mimic the fog calculations provided by OpenGL ES 1.1.

When fog is enabled, the fog component is calculated and clamped to a range from `0.0` to `1.0`. Then, the fog value is used as a blending factor between the computed fragment color and the fog color.

## Topics

### Enabling Fog
- [var enabled: GLboolean](glkeffectpropertyfog/enabled.md)
  A Boolean value that indicates whether fog is applied to the fragment color.
### Choosing the Fog Mode
- [var mode: GLint](glkeffectpropertyfog/mode.md)
  The algorithm used to compute the density of the fog applied to the fragment color.
### Fog Properties
- [var color: GLKVector4](glkeffectpropertyfog/color.md)
  The color of the fog at maximum density.
- [var density: GLfloat](glkeffectpropertyfog/density.md)
  The rate at which the fog exponent increases.
- [var start: GLfloat](glkeffectpropertyfog/start.md)
  The minimum distance in eye coordinates before fog is applied to the fragment color.
- [var end: GLfloat](glkeffectpropertyfog/end.md)
  The distance in eye coordinates where fog completely covers the color fragment.
### Constants
- [enum GLKFogMode](glkfogmode.md)
  A mode that describes how the fog component is calculated for the fragment.

## Relationships

### Inherits From
- [GLKEffectProperty](glkeffectproperty.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GLKEffectProperty](glkeffectproperty.md)
  The abstract superclass for configuration information used in GLKit rendering effects.
- [class GLKEffectPropertyLight](glkeffectpropertylight.md)
  Lighting information for use in GLKit rendering effects.
- [class GLKEffectPropertyTexture](glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog)*