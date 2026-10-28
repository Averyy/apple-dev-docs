# CVOpenGLTextureCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Performs internal housekeeping/recycling operations on the cache.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureCacheFlush(_ textureCache: CVOpenGLTextureCache, _ options: CVOptionFlags)
```

```c
extern void CVOpenGLTextureCacheFlush(CVOpenGLTextureCacheRef textureCache, CVOptionFlags options);
```

## Discussion

This call must be made periodically to give the texture cache a chance to make OpenGL calls on the OpenGL context used to create it in order to perform its required housekeeping operations.

## Parameters

- `textureCache`: The texture cache object to flush.
- `options`: Currently unused, set to 0.

## See Also

### Functions
- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](./cvopengltexturecachecreatetexturefromimage%28_,_,_,_,_%29.md)
  Creates a CVOpenGLTexture object from an existing [CVImageBuffer](./cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](./cvopengltexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a the texture cache.
- [CVOpenGLTextureCacheRetain](./cvopengltexturecacheretain.md)
  Retains a texture cache object.
- [CVOpenGLTextureCacheRelease](./cvopengltexturecacherelease.md)
  Releases a texture cache object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecacheflush(_:_:))*