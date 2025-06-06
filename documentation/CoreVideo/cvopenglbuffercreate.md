# CVOpenGLBufferCreate(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferCreate(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ attributes: CFDictionary?, _ bufferOut: UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

## Parameters

- `allocator`: The allocator to use to create the Core Video OpenGL buffer. Pass   to specify the default allocator.
- `width`: The width of the buffer in pixels.
- `height`: The height of the buffer in pixels.
- `attributes`: A Core Foundation dictionary containing other desired attributes of the buffer (texture target, internal format, max mipmap level, etc.). May be  . The following attribute values are assumed if you do not explicitly define them:
- `bufferOut`: On output,   points to the newly created OpenGL buffer.

## See Also

- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](cvopenglbufferattach(_:_:_:_:_:).md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](cvopenglbuffergetattributes(_:).md)
  Obtains the attributes of a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetTypeID() -> CFTypeID](cvopenglbuffergettypeid().md)
  Obtains the Core Foundation type ID for the OpenGL buffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbuffercreate(_:_:_:_:_:))*