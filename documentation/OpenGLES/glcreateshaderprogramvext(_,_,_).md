# glCreateShaderProgramvEXT(_:_:_:)

**Framework**: OpenGL ES  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- Mac Catalyst 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func glCreateShaderProgramvEXT(_ type: GLenum, _ count: GLsizei, _ strings: UnsafePointer<UnsafePointer<GLchar>?>!) -> GLuint
```

```c
extern GLuint glCreateShaderProgramvEXT(GLenum type, GLsizei count, const GLchar * const*strings);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glcreateshaderprogramvext(_:_:_:))*