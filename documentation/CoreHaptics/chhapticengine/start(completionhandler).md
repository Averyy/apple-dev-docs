# start(completionHandler:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method

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
func start(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func start() async throws
```

```objc
- (void) startWithCompletionHandler:(CHHapticCompletionHandler) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func start() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: The closure the system calls to indicate whether the server started successfully or encountered an error.

## See Also

### Starting and Stopping the Haptic Engine
- [func start() throws](./start%28%29.md)
  Synchronously starts the haptic engine.
- [func stop(completionHandler: (((any Error)?) -> Void)?)](./stop%28completionhandler%29.md)
  Asynchronously stops the haptic engine and executes the completion handler once the engine has stopped.
- [CHHapticEngine.CompletionHandler](./completionhandler.md)
  A typealias for a completion handler that the engine calls after starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/start(completionhandler:))*