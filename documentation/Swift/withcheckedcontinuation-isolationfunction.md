# withCheckedContinuation(isolation:function:_:)

**Framework**: Swift  
**Kind**: func

Invokes the passed in closure with a checked continuation for the current task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withCheckedContinuation<T>(isolation: isolated (any Actor)? = #isolation, function: String = #function, _ body: (CheckedContinuation<T, Never>) -> Void) async -> sending T
```

#### Return Value

The value continuation is resumed with.

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

The checked continuation offers detection of misuse, and dropping the last reference to it, without having resumed it will trigger a warning. Resuming a continuation twice is also diagnosed and will cause a crash.

> **Note**: `withCheckedThrowingContinuation(function:_:)`

> **Note**: `withUnsafeContinuation(function:_:)`

> **Note**: `withUnsafeThrowingContinuation(function:_:)`

## Parameters

- `function`: A string identifying the declaration that is the notional   source for the continuation, used to identify the continuation in   runtime diagnostics related to misuse of this continuation.
- `body`: A closure that takes a   parameter.

## See Also

- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcheckedcontinuation(isolation:function:_:))*