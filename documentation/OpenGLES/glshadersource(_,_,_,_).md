# glShaderSource(_:_:_:_:)

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
func glShaderSource(_ shader: GLuint, _ count: GLsizei, _ string: UnsafePointer<UnsafePointer<GLchar>?>!, _ length: UnsafePointer<GLint>!)
```

```c
extern void glShaderSource(GLuint shader, GLsizei count, const GLchar * const*string, const GLint *length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glshadersource(_:_:_:_:))*