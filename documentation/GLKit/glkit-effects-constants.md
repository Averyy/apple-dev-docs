# GLKit Effects Constants

**Framework**: GLKit

#### Overview

GLKit effects implement shaders to perform their calculations. These shaders require vertex data to be provided by your application. All of the effects provided by GLKit use a consistent set of indices to reference vertex data provided by your application. When your application enables a vertex attribute array by calling the `glEnableVertexAttribArray` function, or specifies the vertex attribute pointer by calling the `glVertexAttribPointer` function, it uses one of these constants to specify the `index` parameter.

## Topics

### Constants
- [enum GLKVertexAttrib](glkvertexattrib.md)
  Values used as indices in OpenGL code to associate vertex data with an attribute in a named shader effect.

## See Also

- [class GLKEffectProperty](glkeffectproperty.md)
  The abstract superclass for configuration information used in GLKit rendering effects.
- [class GLKEffectPropertyFog](glkeffectpropertyfog.md)
  Fog drawing information for use in GLKit rendering effects.
- [class GLKEffectPropertyLight](glkeffectpropertylight.md)
  Lighting information for use in GLKit rendering effects.
- [class GLKEffectPropertyTexture](glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkit-effects-constants)*