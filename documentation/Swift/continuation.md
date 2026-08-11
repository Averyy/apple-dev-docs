# Continuation

**Framework**: Swift  
**Kind**: struct

A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.

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
@frozen
struct Continuation<Success, Failure> where Failure : Error, Success : ~Copyable
```

#### Overview

Unlike `CheckedContinuation`, which detects misuse at runtime, `Continuation` uses non-copyable semantics to enforce correct usage.

The continuation must only ever be resumed **exactly-once**. The compiler will prevent attempts from resuming the continuation more than once.

If a `Continuation` is destroyed without being resumed, the program traps with a diagnostic message indicating where the continuation was created. Because it is noncopyable, the compiler prevents accidental copies, and the `consuming` resume methods ensure the continuation can only be used once.

To create a continuation call [`withContinuation(of:throwing:_:)`](withcontinuation(of:throwing:_:).md).

To resume the task, suspended on a continuation, call [`resume(returning:)`](continuation/resume(returning:)-5fa8w.md), [`resume(throwing:)`](continuation/resume(throwing:).md), [`resume(with:)`](continuation/resume(with:).md), or [`resume()`](continuation/resume().md).

> **Note**: [`CheckedContinuation`](checkedcontinuation.md)

## Topics

### Instance Methods
- [func resume()](continuation/resume.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(returning: consuming sending Success)](continuation/resume(returning:)-5fa8w.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(returning: consuming sending Success)](continuation/resume(returning:)-8uw9b.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(throwing: Failure)](continuation/resume(throwing:).md)
  Resume the task awaiting the continuation by having it throw an error from its suspension point
- [func resume(with: consuming sending Result<Success, Failure>)](continuation/resume(with:).md)
  Resume the task awaiting the continuation by having it either return or throw an error based on the state of the given `Result` value

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [func withContinuation<Success>(of: Success.Type, (consuming Continuation<Success, Never>) -> Void) async -> sending Success](withcontinuation(of:_:).md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [func withContinuation<Success, Failure>(of: Success.Type, throwing: Failure.Type, (consuming Continuation<Success, Failure>) -> Void) async throws(Failure) -> sending Success](withcontinuation(of:throwing:_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuation)*