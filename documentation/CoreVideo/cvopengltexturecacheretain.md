# CVOpenGLTextureCacheRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a texture cache object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern CVOpenGLTextureCacheRefCVOpenGLTextureCacheRetain(CVOpenGLTextureCacheRef textureCache);
```

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), but is `NULL` safe.

## Parameters

- `textureCache`: The texture cache object that you want to retain.

## See Also

### Functions
- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](./cvopengltexturecachecreate%28_,_,_,_,_,_%29.md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](./cvopengltexturecachecreatetexturefromimage%28_,_,_,_,_%29.md)
  Creates a CVOpenGLTexture object from an existing [CVImageBuffer](./cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](./cvopengltexturecacheflush%28_,_%29.md)
  Performs internal housekeeping/recycling operations on the cache.
- [CVOpenGLTextureCacheRelease](./cvopengltexturecacherelease.md)
  Releases a texture cache object.
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](./cvopengltexturecachegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a the texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecacheretain)*