# CVOpenGLBufferPoolGetTypeID()

**Framework**: Core Video  
**Kind**: func

Obtains the Core Foundation ID for the OpenGL buffer pool type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferPoolGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation ID for this data type.

## See Also

- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](cvopenglbufferpoolcreate(_:_:_:_:).md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbufferpoolcreateopenglbuffer(_:_:_:).md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetattributes(_:).md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetopenglbufferattributes(_:).md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolgettypeid())*