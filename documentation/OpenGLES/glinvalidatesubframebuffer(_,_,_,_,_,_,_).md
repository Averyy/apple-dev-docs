# glInvalidateSubFramebuffer(_:_:_:_:_:_:_:)

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
func glInvalidateSubFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>!, _ x: GLint, _ y: GLint, _ width: GLsizei, _ height: GLsizei)
```

```c
extern void glInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glinvalidatesubframebuffer(_:_:_:_:_:_:_:))*