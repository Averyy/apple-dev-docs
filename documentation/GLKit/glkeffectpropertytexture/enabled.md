# enabled

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether this texture is used to texture drawn primitives.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var enabled: GLboolean { get set }
```

#### Discussion

If the value is `GL_TRUE`, then the texture is applied to the primitive. If the value is `GL_FALSE`, the texture is skipped. The default value is `GL_TRUE`.

## See Also

- [var envMode: GLKTextureEnvMode](glkeffectpropertytexture/envmode.md)
  The mode the texture uses to compute its output fragment color. See [`GLKTextureEnvMode`](glktextureenvmode.md).
- [var name: GLuint](glkeffectpropertytexture/name.md)
  The OpenGL name for the texture being sampled by this texture stage.
- [var target: GLKTextureTarget](glkeffectpropertytexture/target.md)
  The kind of texture pointed to by the texture stage. See [`GLKTextureTarget`](glktexturetarget.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/enabled)*