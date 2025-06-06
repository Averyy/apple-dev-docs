# CVOpenGLESTextureCacheGetTypeID()

**Framework**: Core Video  
**Kind**: func

Returns the Core Foundation type identifier for a Core Video texture cache.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func CVOpenGLESTextureCacheGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation type identifier for the `CVOpenGLESTextureCacheRef` type.

## See Also

- [func CVOpenGLESTextureCacheCreate(CFAllocator?, CFDictionary?, CVEAGLContext, CFDictionary?, UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](cvopenglestexturecachecreate(_:_:_:_:_:).md)
  Creates a new Core Video texture cache.
- [func CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator?, CVOpenGLESTextureCache, CVImageBuffer, CFDictionary?, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](cvopenglestexturecachecreatetexturefromimage(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a [`CVOpenGLESTexture`](cvopenglestexture.md) object from an existing [`CVImageBuffer`](cvimagebuffer.md).
- [func CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache, CVOptionFlags)](cvopenglestexturecacheflush(_:_:).md)
  Performs internal housekeeping/recycling operations on a texture cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglestexturecachegettypeid())*