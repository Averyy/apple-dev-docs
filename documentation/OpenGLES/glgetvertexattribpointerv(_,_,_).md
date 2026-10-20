# glGetVertexAttribPointerv(_:_:_:)

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
func glGetVertexAttribPointerv(_ index: GLuint, _ pname: GLenum, _ pointer: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

```c
extern void glGetVertexAttribPointerv(GLuint index, GLenum pname, GLvoid **pointer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glgetvertexattribpointerv(_:_:_:))*