# CVOpenGLBufferRetain

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retains a Core Video OpenGL buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern CVOpenGLBufferRefCVOpenGLBufferRetain(CVOpenGLBufferRef buffer);
```

## Return Value

For convenience, the OpenGL buffer that was retained.

## Discussion

This function is equivalent to `CFRetain`, but is `NULL` safe.

## Parameters

- `buffer`: The OpenGL Buffer that you want to retain.

## See Also

### Functions
- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbuffercreate%28_,_,_,_,_%29.md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](./cvopenglbufferattach%28_,_,_,_,_%29.md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](./cvopenglbuffergetattributes%28_%29.md)
  Obtains the attributes of a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetTypeID() -> CFTypeID](./cvopenglbuffergettypeid%28%29.md)
  Obtains the Core Foundation type ID for the OpenGL buffer type.
- [CVOpenGLBufferRelease](./cvopenglbufferrelease.md)
  Releases a Core Video OpenGL buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferretain)*