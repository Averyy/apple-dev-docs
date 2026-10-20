# CHHapticEngine.CompletionHandler

**Framework**: Core Haptics  
**Kind**: typealias  
**Role**: Type Alias

A typealias for a completion handler that the engine calls after starting or stopping.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionHandler = ((any Error)?) -> Void
```

```c
typedef void (^)(NSError *) CHHapticCompletionHandler;
```

## See Also

### Starting and Stopping the Haptic Engine
- [func start() throws](./start%28%29.md)
  Synchronously starts the haptic engine.
- [func start(completionHandler: (((any Error)?) -> Void)?)](./start%28completionhandler%29.md)
  Asynchronously starts the haptic engine.
- [func stop(completionHandler: (((any Error)?) -> Void)?)](./stop%28completionhandler%29.md)
  Asynchronously stops the haptic engine and executes the completion handler once the engine has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/completionhandler)*