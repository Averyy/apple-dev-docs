# CVOpenGLTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func

Returns the Core Foundation type identifier for a the texture cache.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureCacheGetTypeID() -> CFTypeID
```

## See Also

- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](cvopengltexturecachecreate(_:_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](cvopengltexturecachecreatetexturefromimage(_:_:_:_:_:).md)
  Creates a CVOpenGLTexture object from an existing [`CVImageBuffer`](cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](cvopengltexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachegettypeid())*