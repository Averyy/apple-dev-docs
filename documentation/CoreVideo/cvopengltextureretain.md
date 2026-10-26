# CVOpenGLTextureRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a Core Video OpenGL texture.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern CVOpenGLTextureRefCVOpenGLTextureRetain(CVOpenGLTextureRef texture);
```

#### Return Value

For convenience, the Core Video OpenGL texture you want to retain.

#### Discussion

This function is equivalent to `CFRetain`, but is `NULL` safe.

## Parameters

- `texture`: The Core Video OpenGL texture that you want to retain.

## See Also

### Retaining and Releasing Textures
- [CVOpenGLTextureRelease](./cvopengltexturerelease.md)
  Releases a Core Video OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltextureretain)*