# name

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The OpenGL name for the texture being sampled by this texture stage.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var name: GLuint { get set }
```

```objc
@property (nonatomic, assign) GLuint name;
```

## See Also

### Configuring Texture Properties
- [var enabled: GLboolean](./enabled.md)
  A Boolean value that indicates whether this texture is used to texture drawn primitives.
- [var envMode: GLKTextureEnvMode](./envmode.md)
  The mode the texture uses to compute its output fragment color. See [`GLKTextureEnvMode`](../glktextureenvmode.md).
- [var target: GLKTextureTarget](./target.md)
  The kind of texture pointed to by the texture stage. See [`GLKTextureTarget`](../glktexturetarget.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/name)*