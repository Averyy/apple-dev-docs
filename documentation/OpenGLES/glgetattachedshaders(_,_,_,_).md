# glGetAttachedShaders(_:_:_:_:)

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
func glGetAttachedShaders(_ program: GLuint, _ maxcount: GLsizei, _ count: UnsafeMutablePointer<GLsizei>!, _ shaders: UnsafeMutablePointer<GLuint>!)
```

```c
extern void glGetAttachedShaders(GLuint program, GLsizei maxcount, GLsizei *count, GLuint *shaders);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetattachedshaders(_:_:_:_:))*