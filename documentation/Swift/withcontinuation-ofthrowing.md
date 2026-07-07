# withContinuation(of:throwing:_:)

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
(nonsending) func withContinuation<Success, Failure>(of: Success.Type = Success.self, throwing: Failure.Type, _ body: (consuming Continuation<Success, Failure>) -> Void) async throws(Failure) -> sending Success where Failure : Error, Success : ~Copyable
```

#### Return Value

The value the continuation is resumed with

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once. The continuation is a noncopyable type, and therefore multiple resume calls are prevented at compile time (as resuming the continuation consumes it). However, if the continuation is dropped without being resumed, the program traps.

## Parameters

- `of`: The `Success` type returned by the continuation
- `throwing`: The `Failure` type that may be thrown
- `body`: A closure that takes a `Continuation` parameter

## See Also

- [struct Continuation](continuation.md)
  A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.
- [func withContinuation<Success>(of: Success.Type, (consuming Continuation<Success, Never>) -> Void) async -> sending Success](withcontinuation(of:_:).md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(function:_:)-13yf6.md)
- [func withCheckedThrowingContinuation<T, E>(function: String, (CheckedContinuation<T, E>) -> Void) async throws(E) -> sending T](withcheckedthrowingcontinuation(function:_:)-2k46m.md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>((UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcontinuation(of:throwing:_:))*