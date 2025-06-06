# CVOpenGLBufferGetAttributes(_:)

**Framework**: Core Video  
**Kind**: func

Obtains the attributes of a Core Video OpenGL buffer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferGetAttributes(_ openGLBuffer: CVOpenGLBuffer) -> Unmanaged<CFDictionary>?
```

#### Return Value

A Core Foundation dictionary containing the OpenGL buffer attributes, or `NULL` if no attributes exist.

## Parameters

- `openGLBuffer`: The OpenGL buffer whose attributes you want to obtain.

## See Also

- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbuffercreate(_:_:_:_:_:).md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](cvopenglbufferattach(_:_:_:_:_:).md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetTypeID() -> CFTypeID](cvopenglbuffergettypeid().md)
  Obtains the Core Foundation type ID for the OpenGL buffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbuffergetattributes(_:))*