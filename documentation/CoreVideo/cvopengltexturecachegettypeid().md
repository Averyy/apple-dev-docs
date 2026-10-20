# CVOpenGLTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier for a the texture cache.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLTextureCacheGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVOpenGLTextureCacheGetTypeID();
```

## See Also

### Functions
- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](./cvopengltexturecachecreatetexturefromimage%28_,_,_,_,_%29.md)
  Creates a CVOpenGLTexture object from an existing [CVImageBuffer](./cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](./cvopengltexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachegettypeid())*