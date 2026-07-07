# withCheckedThrowingContinuation(function:_:)

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
@abi(nonisolated(nonsending) func withCheckedThrowingContinuationNonisolatedNonsending<T, E>(function: String, _ body: (CheckedContinuation<T, E>) -> Void) async throws(E) -> sending T where E : Error) nonisolated(nonsending) func withCheckedThrowingContinuation<T, E>(function: String = #function, _ body: (CheckedContinuation<T, E>) -> Void) async throws(E) -> sending T where E : Error
```

#### Return Value

The value continuation is resumed with.

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

If `resume(throwing:)` is called on the continuation, this function throws that error.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

The checked continuation offers detection of misuse, and dropping the last reference to it, without having resumed it will trigger a warning. Resuming a continuation twice is also diagnosed and will cause a crash.

> **Note**: `withCheckedContinuation(function:_:)`

> **Note**: `withUnsafeContinuation(function:_:)`

> **Note**: `withUnsafeThrowingContinuation(function:_:)`

## Parameters

- `function`: A string identifying the declaration that is the notional source for the continuation, used to identify the continuation in runtime diagnostics related to misuse of this continuation.
- `body`: A closure that takes a `CheckedContinuation` parameter.

## See Also

- [struct Continuation](continuation.md)
  A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.
- [func withContinuation<Success>(of: Success.Type, (consuming Continuation<Success, Never>) -> Void) async -> sending Success](withcontinuation(of:_:).md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [func withContinuation<Success, Failure>(of: Success.Type, throwing: Failure.Type, (consuming Continuation<Success, Failure>) -> Void) async throws(Failure) -> sending Success](withcontinuation(of:throwing:_:).md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(function:_:)-13yf6.md)
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>((UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcheckedthrowingcontinuation(function:_:)-2k46m)*