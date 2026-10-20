# CVOpenGLESTextureCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Performs internal housekeeping/recycling operations on a texture cache.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLESTextureCacheFlush(_ textureCache: CVOpenGLESTextureCache, _ options: CVOptionFlags)
```

```c
extern void CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCacheRef textureCache, CVOptionFlags options);
```

#### Discussion

The texture cache automatically flushes currently unused resources when you call the [`CVOpenGLESTextureCacheCreateTextureFromImage(_:_:_:_:_:_:_:_:_:_:_:_:)`](./cvopenglestexturecachecreatetexturefromimage%28_,_,_,_,_,_,_,_,_,_,_,_%29.md) function, but can you can also flush the cache explicitly by calling this function. The EAGLContext associated with the cache may be used to delete or unbind textures.

## Parameters

- `textureCache`: The texture cache object to flush.
- `options`: Options for the flush operation. This parameter is currently unused and should be set to `0`.

## See Also

### Functions
- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](./cvopenglestexturecachecreate%28_,_,_,_,_%29.md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](./cvopenglestexturecachecreatetexturefromimage%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a [`CVOpenGLESTexture`](./cvopenglestexture.md) object from an existing [`CVImageBuffer`](./cvimagebuffer.md).
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](./cvopenglestexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a Core Video texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecacheflush(_:_:))*