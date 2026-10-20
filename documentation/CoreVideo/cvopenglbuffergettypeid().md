# CVOpenGLBufferGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Obtains the Core Foundation type ID for the OpenGL buffer type.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLBufferGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVOpenGLBufferGetTypeID();
```

#### Return Value

The Core Foundation ID for this data type.

## See Also

### Functions
- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbuffercreate%28_,_,_,_,_%29.md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferAttach(CVOpenGLBuffer, CGLContextObj, GLenum, GLint, GLint) -> CVReturn](./cvopenglbufferattach%28_,_,_,_,_%29.md)
  Attaches an OpenGL context to a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](./cvopenglbuffergetattributes%28_%29.md)
  Obtains the attributes of a Core Video OpenGL buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbuffergettypeid())*