# kCVOpenGLBufferPoolMaximumBufferAgeKey

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

The maximum time that unused buffers should be kept before they are deallocated (type `CFAbsoluteTime`).

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLBufferPoolMaximumBufferAgeKey: CFString
```

```c
extern CFStringRef const kCVOpenGLBufferPoolMaximumBufferAgeKey;
```

## See Also

### Constants
- [let kCVOpenGLBufferPoolMinimumBufferCountKey: CFString](./kcvopenglbufferpoolminimumbuffercountkey.md)
  The minimum number of buffers to be kept in the pool (type `CFNumber`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopenglbufferpoolmaximumbufferagekey)*