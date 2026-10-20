# glUniformMatrix4fv(_:_:_:_:)

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
func glUniformMatrix4fv(_ location: GLint, _ count: GLsizei, _ transpose: GLboolean, _ value: UnsafePointer<GLfloat>!)
```

```c
extern void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/gluniformmatrix4fv(_:_:_:_:))*