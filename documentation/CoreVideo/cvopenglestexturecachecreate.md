# CVOpenGLESTextureCacheCreate(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new Core Video texture cache.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ eaglContext: CVEAGLContext, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn
```

#### Return Value

Upon successful creation of the texture cache, this function returns [`kCVReturnSuccess`](kcvreturnsuccess.md).

## Parameters

- `allocator`: The   to use for allocating the texture cache. This parameter can be  .
- `cacheAttributes`: A   containing the attributes of the texture cache itself. This parameter can be  .
- `eaglContext`: The OpenGLES 2.0 context into which the texture objects will be created. OpenGLES 1.x contexts are not supported.
- `textureAttributes`: A   containing the attributes to be used for creating the   objects. This parameter can be  .
- `cacheOut`: A pointer to a   where the newly created texture cache will be placed.

## See Also

- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a [`CVOpenGLESTexture`](cvopenglestexture.md) object from an existing [`CVImageBuffer`](cvimagebuffer.md).
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](cvopenglestexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on a texture cache.
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](cvopenglestexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecachecreate(_:_:_:_:_:))*