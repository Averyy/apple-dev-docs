# target

**Framework**: GLKit  
**Kind**: property

The kind of texture pointed to by the texture stage. See [`GLKTextureTarget`](glktexturetarget.md).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var target: GLKTextureTarget { get set }
```

#### Discussion

The default value is [`GLKTextureTarget.target2D`](glktexturetarget/target2d.md).

## See Also

- [var enabled: GLboolean](glkeffectpropertytexture/enabled.md)
  A Boolean value that indicates whether this texture is used to texture drawn primitives.
- [var envMode: GLKTextureEnvMode](glkeffectpropertytexture/envmode.md)
  The mode the texture uses to compute its output fragment color. See [`GLKTextureEnvMode`](glktextureenvmode.md).
- [var name: GLuint](glkeffectpropertytexture/name.md)
  The OpenGL name for the texture being sampled by this texture stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture/target)*