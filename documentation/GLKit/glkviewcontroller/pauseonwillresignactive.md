# pauseOnWillResignActive

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view controller automatically pauses the rendering loop when the application resigns the active state.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var pauseOnWillResignActive: Bool { get set }
```

```objc
@property (nonatomic) BOOL pauseOnWillResignActive;
```

## Discussion

The default value is [`true`](../../Swift/true.md). If your application sets this to [`false`](../../Swift/false.md), it must explicitly set the [`isPaused`](./ispaused.md) property to [`true`](../../Swift/true.md) when the application resigns the active state.

## See Also

### Controlling Frame Updates
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the rendering loop is paused.
- [var resumeOnDidBecomeActive: Bool](./resumeondidbecomeactive.md)
  A Boolean value that indicates whether the view controller automatically resumes the rendering loop when the application becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/pauseonwillresignactive)*