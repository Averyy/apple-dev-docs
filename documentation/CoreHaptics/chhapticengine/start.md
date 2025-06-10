# start()

**Framework**: Core Haptics  
**Kind**: method

Synchronously starts the haptic engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func start() throws
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)
- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)

#### Discussion

This method blocks all subsequent event processing on the current thread until the engine has started. It throws an error if the engine can’t start.

## See Also

- [func start(completionHandler: (((any Error)?) -> Void)?)](chhapticengine/start(completionhandler:).md)
  Asynchronously starts the haptic engine.
- [func stop(completionHandler: (((any Error)?) -> Void)?)](chhapticengine/stop(completionhandler:).md)
  Asynchronously stops the haptic engine and executes the completion handler once the engine has stopped.
- [CHHapticEngine.CompletionHandler](chhapticengine/completionhandler.md)
  A typealias for a completion handler that the engine calls after starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/start())*