# CVOpenGLTextureCacheCreateTextureFromImage(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a CVOpenGLTexture object from an existing [`CVImageBuffer`](cvimagebuffer-q40.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVOpenGLTextureCache, _ sourceImage: CVImageBuffer, _ attributes: CFDictionary?, _ textureOut: UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn
```

#### Return Value

Returns [`kCVReturnSuccess`](kcvreturnsuccess.md) on success.

## Parameters

- `allocator`: The   to use for allocating the   object.  May be  .
- `textureCache`: The texture cache object that will manage the texture.
- `sourceImage`: The source   for which to create an  .
- `attributes`: The desired buffer attributes for the  .
- `textureOut`: Upon return, contains the newly created texture.

## See Also

- [func CVOpenGLTextureCacheCreate(CFAllocator?, CFDictionary?, CGLContextObj, CGLPixelFormatObj, CFDictionary?, UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn](cvopengltexturecachecreate(_:_:_:_:_:_:).md)
  Creates a new texture cache.
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](cvopengltexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on the cache.
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](cvopengltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a the texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachecreatetexturefromimage(_:_:_:_:_:))*