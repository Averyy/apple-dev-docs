# glGetTransformFeedbackVarying(_:_:_:_:_:_:_:)

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
func glGetTransformFeedbackVarying(_ program: GLuint, _ index: GLuint, _ bufSize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ size: UnsafeMutablePointer<GLsizei>!, _ type: UnsafeMutablePointer<GLenum>!, _ name: UnsafeMutablePointer<GLchar>!)
```

```c
extern void glGetTransformFeedbackVarying(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgettransformfeedbackvarying(_:_:_:_:_:_:_:))*