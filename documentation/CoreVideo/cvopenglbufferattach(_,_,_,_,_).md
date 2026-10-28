# CVOpenGLBufferAttach(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Attaches an OpenGL context to a Core Video OpenGL buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
func CVOpenGLBufferAttach(_ openGLBuffer: CVOpenGLBuffer, _ cglContext: CGLContextObj, _ face: GLenum, _ level: GLint, _ screen: GLint) -> CVReturn
```

```c
extern CVReturn CVOpenGLBufferAttach(CVOpenGLBufferRef openGLBuffer, CGLContextObj cglContext, GLenum face, GLint level, GLint screen);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Parameters

- `openGLBuffer`: The buffer you want to attach an OpenGL context to.
- `cglContext`: The OpenGL context you want to attach.
- `face`: The OpenGL face enumeration (`0` for non-cube maps.)
- `level`: The mipmap level for drawing in the OpenGL context. This value cannot exceed the maximum mipmap level for this buffer.
- `screen`: The virtual screen number you want to use for this context.

## See Also

### Related Documentation
- [Core Video Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
### Functions
- [func CVOpenGLBufferCreate(CFAllocator?, Int, Int, CFDictionary?, UnsafeMutablePointer<CVOpenGLBuffer?>) -> CVReturn](./cvopenglbuffercreate%28_,_,_,_,_%29.md)
  Creates a new Core Video OpenGL buffer that can be used for OpenGL rendering purposes
- [func CVOpenGLBufferGetAttributes(CVOpenGLBuffer) -> Unmanaged<CFDictionary>?](./cvopenglbuffergetattributes%28_%29.md)
  Obtains the attributes of a Core Video OpenGL buffer.
- [func CVOpenGLBufferGetTypeID() -> CFTypeID](./cvopenglbuffergettypeid%28%29.md)
  Obtains the Core Foundation type ID for the OpenGL buffer type.
- [CVOpenGLBufferRetain](./cvopenglbufferretain.md)
  Retains a Core Video OpenGL buffer.
- [CVOpenGLBufferRelease](./cvopenglbufferrelease.md)
  Releases a Core Video OpenGL buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvopenglbufferattach(_:_:_:_:_:))*