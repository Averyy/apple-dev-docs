# withContinuation(of:_:)

**Framework**: Swift  
**Kind**: func

Invokes the passed in closure with a non-copyable continuation for the current task.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func withContinuation<Success>(of: Success.Type = Success.self, _ body: (consuming Continuation<Success, Never>) -> Void) async -> sending Success where Success : ~Copyable
```

#### Return Value

The value the continuation is resumed with

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once. The continuation is a noncopyable type, and therefore multiple resume calls are prevented at compile time (as resuming the continuation consumes it). However, if the continuation is dropped without being resumed, the program traps.

## Parameters

- `of`: The `Success` type returned by the continuation
- `body`: A closure that takes a `Continuation` parameter


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcontinuation(of:_:))*