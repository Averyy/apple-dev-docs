# glGetShaderSource(_:_:_:_:)

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
func glGetShaderSource(_ shader: GLuint, _ bufsize: GLsizei, _ length: UnsafeMutablePointer<GLsizei>!, _ source: UnsafeMutablePointer<GLchar>!)
```

```c
extern void glGetShaderSource(GLuint shader, GLsizei bufsize, GLsizei *length, GLchar *source);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetshadersource(_:_:_:_:))*