# glMapBufferRange(_:_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 7.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glMapBufferRange(_ target: GLenum, _ offset: GLintptr, _ length: GLsizeiptr, _ access: GLbitfield) -> UnsafeMutableRawPointer!
```

```c
extern GLvoid *glMapBufferRange(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glmapbufferrange(_:_:_:_:))*