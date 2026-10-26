# CVOpenGLBufferRelease

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Releases a Core Video OpenGL buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```c
extern void CVOpenGLBufferRelease(CVOpenGLBufferRef buffer);
```

#### Discussion

This function is equivalent to `CFRelease`, but is `NULL` safe.

## Parameters

- `buffer`: The OpenGL buffer that you want to release.

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
- [CVOpenGLBufferRetain](./cvopenglbufferretain.md)
  Retains a Core Video OpenGL buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferrelease)*