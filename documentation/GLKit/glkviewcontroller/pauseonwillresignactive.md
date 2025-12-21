# pauseOnWillResignActive

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether the view controller automatically pauses the rendering loop when the application resigns the active state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var pauseOnWillResignActive: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If your application sets this to [`false`](https://developer.apple.com/documentation/Swift/false), it must explicitly set the [`isPaused`](glkviewcontroller/ispaused.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when the application resigns the active state.

## See Also

- [var isPaused: Bool](glkviewcontroller/ispaused.md)
  A Boolean value that indicates whether the rendering loop is paused.
- [var resumeOnDidBecomeActive: Bool](glkviewcontroller/resumeondidbecomeactive.md)
  A Boolean value that indicates whether the view controller automatically resumes the rendering loop when the application becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/pauseonwillresignactive)*