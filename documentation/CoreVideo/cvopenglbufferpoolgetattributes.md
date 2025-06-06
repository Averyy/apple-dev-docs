# CVOpenGLBufferPoolGetAttributes(_:)

**Framework**: Core Video  
**Kind**: func

Returns the pool attributes dictionary for an Open GL buffer pool.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferPoolGetAttributes(_ pool: CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?
```

#### Return Value

The buffer-pool attributes Core Foundation dictionary, or `NULL` on failure.

## Parameters

- `pool`: The OpenGL buffer pool containing the attributes to be retrieved.

## See Also

- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](cvopenglbufferpoolcreate(_:_:_:_:).md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbufferpoolcreateopenglbuffer(_:_:_:).md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetopenglbufferattributes(_:).md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](cvopenglbufferpoolgettypeid().md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolgetattributes(_:))*