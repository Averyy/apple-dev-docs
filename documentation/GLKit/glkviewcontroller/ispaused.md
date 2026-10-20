# isPaused

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the rendering loop is paused.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

## See Also

### Controlling Frame Updates
- [var pauseOnWillResignActive: Bool](./pauseonwillresignactive.md)
  A Boolean value that indicates whether the view controller automatically pauses the rendering loop when the application resigns the active state.
- [var resumeOnDidBecomeActive: Bool](./resumeondidbecomeactive.md)
  A Boolean value that indicates whether the view controller automatically resumes the rendering loop when the application becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/ispaused)*