# CVOpenGLBufferPoolCreate(_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new OpenGL buffer pool.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferPoolCreate(_ allocator: CFAllocator?, _ poolAttributes: CFDictionary?, _ openGLBufferAttributes: CFDictionary?, _ poolOut: UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn
```

#### Return Value

A Core Video result code. See[`Core Video Constants`](core-video-constants.md) for possible values.

## Parameters

- `allocator`: The allocator to use for allocating this buffer pool. Pass   to specify the default allocator.
- `poolAttributes`: A Core Foundation dictionary containing the attributes to be used for the pool itself.
- `openGLBufferAttributes`: A Core Foundation dictionary containing the attributes to be used for creating new OpenGL buffers within the pool.
- `poolOut`: On output,   points to the new OpenGL buffer pool.

## See Also

- [func CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator?, CVOpenGLBufferPool, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbufferpoolcreateopenglbuffer(_:_:_:).md)
  Creates a new OpenGL buffer from an OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetattributes(_:).md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetopenglbufferattributes(_:).md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](cvopenglbufferpoolgettypeid().md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolcreate(_:_:_:_:))*