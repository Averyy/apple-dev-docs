# glClientWaitSync(_:_:_:)

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
func glClientWaitSync(_ sync: GLsync!, _ flags: GLbitfield, _ timeout: GLuint64) -> GLenum
```

```c
extern GLenum glClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glclientwaitsync(_:_:_:))*