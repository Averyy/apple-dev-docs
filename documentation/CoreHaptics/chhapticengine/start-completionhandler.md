# start(completionHandler:)

**Framework**: Core Haptics  
**Kind**: method

Asynchronously starts the haptic engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func start() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func start() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func start() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The closure the system calls to indicate whether the server started successfully or encountered an error.

## See Also

- [func start() throws](chhapticengine/start.md)
  Synchronously starts the haptic engine.
- [func stop(completionHandler: CHHapticEngine.CompletionHandler?)](chhapticengine/stop(completionhandler:).md)
  Asynchronously stops the haptic engine and executes the completion handler once the engine has stopped.
- [CHHapticEngine.CompletionHandler](chhapticengine/completionhandler.md)
  A typealias for a completion handler that the engine calls after starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/start(completionhandler:))*