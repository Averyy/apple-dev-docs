# CVOpenGLBufferPoolCreateOpenGLBuffer(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new OpenGL buffer from an OpenGL buffer pool.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferPoolCreateOpenGLBuffer(_ allocator: CFAllocator?, _ openGLBufferPool: CVOpenGLBufferPool, _ openGLBufferOut: UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

The function creates a new OpenGL buffer using the OpenGL buffer attributes specified in the [`CVOpenGLBufferPoolCreate(_:_:_:_:)`](cvopenglbufferpoolcreate(_:_:_:_:).md) call. This buffer has default attachments as specified in the `openGLBufferAttributes` parameter of [`CVOpenGLBufferPoolCreate(_:_:_:_:)`](cvopenglbufferpoolcreate(_:_:_:_:).md) (using either the `kCVBufferPropagatedAttachmentsKey` or `kCVBufferNonPropagatedAttachmentsKey` attributes).

## Parameters

- `allocator`: The allocator to use for creating the buffer.  May be   to specify the default allocator.
- `openGLBufferPool`: The OpenGL buffer pool that should create the new OpenGL buffer.
- `openGLBufferOut`: On output,   points to the new OpenGL buffer.

## See Also

- [func CVOpenGLBufferPoolCreate(CFAllocator?, CFDictionary?, CFDictionary?, UnsafeMutablePointer<CVOpenGLBufferPool?>) -> CVReturn](cvopenglbufferpoolcreate(_:_:_:_:).md)
  Creates a new OpenGL buffer pool.
- [func CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetattributes(_:).md)
  Returns the pool attributes dictionary for an Open GL buffer pool.
- [func CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool) -> Unmanaged<CFDictionary>?](cvopenglbufferpoolgetopenglbufferattributes(_:).md)
  Returns the attributes of OpenGL buffers that will be created from a buffer pool.
- [func CVOpenGLBufferPoolGetTypeID() -> CFTypeID](cvopenglbufferpoolgettypeid().md)
  Obtains the Core Foundation ID for the OpenGL buffer pool type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolcreateopenglbuffer(_:_:_:))*