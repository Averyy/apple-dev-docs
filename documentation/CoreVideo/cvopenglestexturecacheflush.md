# CVOpenGLESTextureCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func

Performs internal housekeeping/recycling operations on a texture cache.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureCacheFlush(_ textureCache: CVOpenGLESTextureCache, _ options: CVOptionFlags)
```

#### Discussion

The texture cache automatically flushes currently unused resources when you call the [`CVOpenGLESTextureCacheCreateTextureFromImage(_:_:_:_:_:_:_:_:_:_:_:_:)`](cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:).md) function, but can you can also flush the cache explicitly by calling this function. The EAGLContext associated with the cache may be used to delete or unbind textures.

## Parameters

- `textureCache`: The texture cache object to flush.
- `options`: Options for the flush operation. This parameter is currently unused and should be set to  .

## See Also

- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](cvopenglestexturecachecreate(_:_:_:_:_:).md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a [`CVOpenGLESTexture`](cvopenglestexture.md) object from an existing [`CVImageBuffer`](cvimagebuffer.md).
- [func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID](cvopenglestexturecachegettypeid().md)
  Returns the Core Foundation type identifier for a Core Video texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecacheflush(_:_:))*