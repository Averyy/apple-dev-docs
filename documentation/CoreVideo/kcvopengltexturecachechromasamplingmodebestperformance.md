# kCVOpenGLTextureCacheChromaSamplingModeBestPerformance

**Framework**: Core Video  
**Kind**: var  
**Role**: Global Variable

Set the chroma sample mode to use the most performant way possible.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

> **Deprecated**: OpenGL/OpenGLES is no longer supported. Use Metal APIs instead. (Define COREVIDEO_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
let kCVOpenGLTextureCacheChromaSamplingModeBestPerformance: CFString
```

```c
extern CFStringRef const kCVOpenGLTextureCacheChromaSamplingModeBestPerformance;
```

## See Also

### Values
- [let kCVOpenGLTextureCacheChromaSamplingModeAutomatic: CFString](./kcvopengltexturecachechromasamplingmodeautomatic.md)
  The default mode if not otherwise specified.
- [let kCVOpenGLTextureCacheChromaSamplingModeHighestQuality: CFString](./kcvopengltexturecachechromasamplingmodehighestquality.md)
  Forces the highest quality regardless of performance impact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvopengltexturecachechromasamplingmodebestperformance)*