# CVOpenGLTextureRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a Core Video OpenGL texture.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern void CVOpenGLTextureRelease(CVOpenGLTextureRef texture);
```

## Discussion

This function is equivalent to `CFRelease`, but is `NULL` safe.

## Parameters

- `texture`: The Core Video OpenGL texture that you want to release.

## See Also

### Retaining and Releasing Textures
- [CVOpenGLTextureRetain](./cvopengltextureretain.md)
  Retains a Core Video OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturerelease)*