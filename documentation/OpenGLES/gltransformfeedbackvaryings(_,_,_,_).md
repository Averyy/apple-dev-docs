# glTransformFeedbackVaryings(_:_:_:_:)

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
func glTransformFeedbackVaryings(_ program: GLuint, _ count: GLsizei, _ varyings: UnsafePointer<UnsafePointer<GLchar>?>!, _ bufferMode: GLenum)
```

```c
extern void glTransformFeedbackVaryings(GLuint program, GLsizei count, const GLchar * const*varyings, GLenum bufferMode);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/gltransformfeedbackvaryings(_:_:_:_:))*