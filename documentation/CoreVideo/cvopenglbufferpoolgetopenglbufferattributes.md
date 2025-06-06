# CVOpenGLBufferPoolGetOpenGLBufferAttributes(_:)

**Framework**: Core Video  
**Kind**: func

Returns the attributes of OpenGL buffers that will be created from a buffer pool.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferPoolGetOpenGLBufferAttributes(_ pool: CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?
```

#### Return Value

The OpenGL buffer attributes Core Foundation dictionary, or `NULL` on failure.

#### Discussion

You can use this function to obtain information about the OpenGL buffers that will be created from the buffer pool.

## Parameters

- `pool`: The OpenGL buffer pool containing the attributes to be retrieved.

## See Also

- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](cvopenglbufferpoolcreate(_:_:_:_:).md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbufferpoolcreateopenglbuffer(_:_:_:).md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetattributes(_:).md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](cvopenglbufferpoolgettypeid().md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolgetopenglbufferattributes(_:))*