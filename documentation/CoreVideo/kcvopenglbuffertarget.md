# kCVOpenGLBufferTarget

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

The OpenGL target for this buffer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLBufferTarget: CFString
```

```c
extern CFStringRef const kCVOpenGLBufferTarget;
```

## See Also

### Constants
- [let kCVOpenGLBufferHeight: CFString](./kcvopenglbufferheight.md)
  The height of the buffer.
- [let kCVOpenGLBufferInternalFormat: CFString](./kcvopenglbufferinternalformat.md)
  The OpenGL internal format of this buffer.
- [let kCVOpenGLBufferMaximumMipmapLevel: CFString](./kcvopenglbuffermaximummipmaplevel.md)
  The maximum mipmap level for this buffer.
- [let kCVOpenGLBufferWidth: CFString](./kcvopenglbufferwidth.md)
  The width of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopenglbuffertarget)*