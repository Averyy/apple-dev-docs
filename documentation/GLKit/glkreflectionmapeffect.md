# GLKReflectionMapEffect

**Framework**: GLKit  
**Kind**: class

A lighting and shading system that supports reflection mapping for use in shader-based OpenGL rendering.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKReflectionMapEffect
```

#### Overview

In addition to any of the properties provided by the [`GLKBaseEffect`](glkbaseeffect.md) class, your application must also configure the properties on the reflection map. The default value of the [`textureOrder`](glkbaseeffect/textureorder.md) property provided by the base effect is modified to include the reflection map as a final texturing stage; your application can modify the value of that property to change the order in which texturing occurs.

The reflection map effect is calculated in accordance to section 2.11.4 of the OpenGL 2.1 specification `GL_REFLECTION_MAP` glTexGen() mode. It requires a cube map texture to define the enclosing envelope from which to reflection map the scene.

## Topics

### Preparing the Reflection Effect
- [func prepareToDraw()](glkreflectionmapeffect/preparetodraw.md)
  Prepares an effect for rendering.
### Effect Properties
- [var textureCubeMap: GLKEffectPropertyTexture](glkreflectionmapeffect/texturecubemap.md)
  The texture map to apply in the reflection stage.
- [var matrix: GLKMatrix3](glkreflectionmapeffect/matrix.md)
  The reflection matrix to apply to the normals of the submitted vertices.

## Relationships

### Inherits From
- [GLKBaseEffect](glkbaseeffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GLKNamedEffect](glknamedeffect.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GLKNamedEffect](glknamedeffect.md)
  A standard interface for objects that provide shader-based OpenGL rendering effects.
- [class GLKBaseEffect](glkbaseeffect.md)
  A simple lighting and shading system for use in shader-based OpenGL rendering.
- [class GLKSkyboxEffect](glkskyboxeffect.md)
  A simple skybox visual effect for use in shader-based OpenGL rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect)*