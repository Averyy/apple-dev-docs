# CVOpenGLTextureCacheCreate(_:_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new texture cache.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVOpenGLTextureCache?>) -> CVReturn
```

#### Return Value

Returns [`kCVReturnSuccess`](kcvreturnsuccess.md) on success.

## Parameters

- `allocator`: The   to use for allocating the cache.  May be NULL.
- `cacheAttributes`: A dictionary specifying options for the cache’s behavior, or   to use default options. For applicable keys and values, see  .
- `cglContext`: The OpenGL context into which the texture objects will be created.
- `cglPixelFormat`: The OpenGL pixel format object used to create the passed in OpenGL context.
- `textureAttributes`: A   containing the attributes to be used for creating the   objects.  May be  .
- `cacheOut`: Upon return, contains the newly created texture cache.

## See Also

- [func CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLTextureCache, CVImageBuffer, CFDictionary?, UnsafeMutablePointer<CVOpenGLTexture?>) -> CVReturn](cvopengltexturecachecreatetexturefromimage(_:_:_:_:_:).md)
  Creates a CVOpenGLTexture object from an existing [`CVImageBuffer`](cvimagebuffer-q40.md).
- [func CVOpenGLTextureCacheFlush(CVOpenGLTextureCache, CVOptionFlags)](cvopengltexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on the cache.
- [func CVOpenGLTextureCacheGetTypeID() -> CFTypeID](cvopengltexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a the texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopengltexturecachecreate(_:_:_:_:_:_:))*