# CVOpenGLBufferGetTypeID()

**Framework**: Core Video  
**Kind**: func

Obtains the Core Foundation type ID for the OpenGL buffer type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CVOpenGLBufferGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation ID for this data type.

## See Also

- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](cvopenglbuffercreate(_:_:_:_:_:).md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](cvopenglbufferattach(_:_:_:_:_:).md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](cvopenglbuffergetattributes(_:).md)
  Obtains the attributes of a Core Video OpenGL buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbuffergettypeid())*