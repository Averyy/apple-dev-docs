# glBufferData(_:_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 3.0+ - Deprecated in 12.0
- iPadOS 3.0+ - Deprecated in 12.0
- Mac Catalyst 3.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glBufferData(_ target: GLenum, _ size: GLsizeiptr, _ data: UnsafeRawPointer!, _ usage: GLenum)
```

```c
extern void glBufferData(GLenum target, GLsizeiptr size, const GLvoid *data, GLenum usage);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glbufferdata(_:_:_:_:))*