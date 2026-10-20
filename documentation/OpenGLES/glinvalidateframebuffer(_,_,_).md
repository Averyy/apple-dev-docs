# glInvalidateFramebuffer(_:_:_:)

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
func glInvalidateFramebuffer(_ target: GLenum, _ numAttachments: GLsizei, _ attachments: UnsafePointer<GLenum>!)
```

```c
extern void glInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/glinvalidateframebuffer(_:_:_:))*