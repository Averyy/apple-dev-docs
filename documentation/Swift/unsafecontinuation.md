# UnsafeContinuation

**Framework**: Swift  
**Kind**: struct

A mechanism to interface between synchronous and asynchronous code, without correctness checking.

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
@frozen
struct UnsafeContinuation<T, E> where E : Error
```

#### Overview

A  is an opaque representation of program state. To create a continuation in asynchronous code, call the `withUnsafeContinuation(_:)` or `withUnsafeThrowingContinuation(_:)` function. To resume the asynchronous task, call the `resume(returning:)`, `resume(throwing:)`, `resume(with:)`, or `resume()` method.

> ❗ **Important**: You must call a resume method exactly once on every execution path throughout the program. Resuming from a continuation more than once is undefined behavior. Never resuming leaves the task in a suspended state indefinitely, and leaks any associated resources.

You must call a resume method exactly once on every execution path throughout the program. Resuming from a continuation more than once is undefined behavior. Never resuming leaves the task in a suspended state indefinitely, and leaks any associated resources.

`CheckedContinuation` performs runtime checks for missing or multiple resume operations. `UnsafeContinuation` avoids enforcing these invariants at runtime because it aims to be a low-overhead mechanism for interfacing Swift tasks with event loops, delegate methods, callbacks, and other non-`async` scheduling mechanisms. However, during development, the ability to verify that the invariants are being upheld in testing is important. Because both types have the same interface, you can replace one with the other in most circumstances, without making other changes.

## Topics

### Instance Methods
- [func resume()](unsafecontinuation/resume.md)
  Resume the task that’s awaiting the continuation by returning.
- [func resume(returning: sending T)](unsafecontinuation/resume(returning:)-41kka.md)
  Resume the task that’s awaiting the continuation by returning the given value.
- [func resume(returning: sending T)](unsafecontinuation/resume(returning:)-8rtni.md)
  Resume the task that’s awaiting the continuation by returning the given value.
- [func resume(throwing: consuming E)](unsafecontinuation/resume(throwing:).md)
  Resume the task that’s awaiting the continuation by throwing the given error.
- [func resume(with: sending Result<T, E>)](unsafecontinuation/resume(with:)-4t59h.md)
  Resume the task that’s awaiting the continuation by returning or throwing the given result value.
- [func resume<Er>(with: sending Result<T, Er>)](unsafecontinuation/resume(with:)-7t959.md)
  Resume the task that’s awaiting the continuation by returning or throwing the given result value.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)

## See Also

- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecontinuation)*