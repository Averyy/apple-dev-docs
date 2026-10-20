# CVOpenGLESTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier for a Core Video texture cache.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVOpenGLESTextureCacheGetTypeID();
```

#### Return Value

The Core Foundation type identifier for the `CVOpenGLESTextureCacheRef` type.

## See Also

### Functions
- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](./cvopenglestexturecachecreate%28_,_,_,_,_%29.md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](./cvopenglestexturecachecreatetexturefromimage%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a [`CVOpenGLESTexture`](./cvopenglestexture.md) object from an existing [`CVImageBuffer`](./cvimagebuffer.md).
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](./cvopenglestexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on a texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecachegettypeid())*