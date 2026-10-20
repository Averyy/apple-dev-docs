# glGetActiveAttrib(_:_:_:_:_:_:_:)

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
func glGetActiveAttrib(_ program: GLuint, _ index: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ size: UnsafeMutablePointer<GLint>!, _ type: UnsafeMutablePointer<GLenum>!, _ name: UnsafeMutablePointer<GLchar>!)
```

```c
extern void glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufsize, GLsizei *length, GLint *size, GLenum *type, GLchar *name);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetactiveattrib(_:_:_:_:_:_:_:))*