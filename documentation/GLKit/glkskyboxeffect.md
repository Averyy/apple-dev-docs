# GLKSkyboxEffect

**Framework**: GLKit  
**Kind**: class

A simple skybox visual effect for use in shader-based OpenGL rendering.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKSkyboxEffect
```

#### Overview

The [`GLKSkyboxEffect`](glkskyboxeffect.md) provides a standard skybox effect for your application. Unlike the [`GLKBaseEffect`](glkbaseeffect.md) class, the skybox does not require your application to configure and submit vertex data. Instead, it creates its own vertex data based on the configuration data you supply.

At initialization time, your application first creates a compatible context and makes it current. Then, it creates new skybox effect, configures its properties, and calls its [`prepareToDraw()`](glkskyboxeffect/preparetodraw().md) method. Binding the effect causes a shader to be compiled and bound to the current context.

At rendering time, your application calls the effect’s [`prepareToDraw()`](glkskyboxeffect/preparetodraw().md) method to prepare the effect and then calls its [`draw()`](glkskyboxeffect/draw().md) method to draw the sky box.

## Topics

### Naming the Effect
- [var label: String?](glkskyboxeffect/label.md)
  A string used to name your effect.
### Preparing the Effect for Rendering
- [func prepareToDraw()](glkskyboxeffect/preparetodraw.md)
  Prepares an effect for rendering.
### Drawing the Skybox
- [func draw()](glkskyboxeffect/draw.md)
  Draws the skybox.
### Configuring the Skybox
- [var textureCubeMap: GLKEffectPropertyTexture](glkskyboxeffect/texturecubemap.md)
  The texture to apply to the skybox.
- [var center: GLKVector3](glkskyboxeffect/center.md)
  The center of the skybox.
- [var xSize: GLfloat](glkskyboxeffect/xsize.md)
  The width of the skybox.
- [var ySize: GLfloat](glkskyboxeffect/ysize.md)
  The height of the skybox.
- [var zSize: GLfloat](glkskyboxeffect/zsize.md)
  The depth of the skybox.
### Setting the Skybox Transform
- [var transform: GLKEffectPropertyTransform](glkskyboxeffect/transform.md)
  The transform applied before drawing the skybox.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class GLKReflectionMapEffect](glkreflectionmapeffect.md)
  A lighting and shading system that supports reflection mapping for use in shader-based OpenGL rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkskyboxeffect)*