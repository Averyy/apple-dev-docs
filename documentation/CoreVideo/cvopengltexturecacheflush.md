# CVOpenGLTextureCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func

Performs internal housekeeping/recycling operations on the cache.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureCacheFlush(_ textureCache: CVOpenGLTextureCache, _ options: CVOptionFlags)
```

#### Discussion

This call must be made periodically to give the texture cache a chance to make OpenGL calls on the OpenGL context used to create it in order to perform its required housekeeping operations.

## Parameters

- `textureCache`: The texture cache object to flush.
- `options`: Currently unused, set to 0.

## See Also

- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](cvopengltexturecachecreate(_:_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](cvopengltexturecachecreatetexturefromimage(_:_:_:_:_:).md)
  Creates a CVOpenGLTexture object from an existing [`CVImageBuffer`](cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](cvopengltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a the texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecacheflush(_:_:))*