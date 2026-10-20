# Continuation

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct Continuation<Success, Failure> where Failure : Error, Success : ~Copyable
```

#### Overview

Unlike `CheckedContinuation`, which detects misuse at runtime, `Continuation` uses non-copyable semantics to enforce correct usage.

The continuation must only ever be resumed **exactly-once**. The compiler will prevent attempts from resuming the continuation more than once.

If a `Continuation` is destroyed without being resumed, the program traps with a diagnostic message indicating where the continuation was created. Because it is noncopyable, the compiler prevents accidental copies, and the `consuming` resume methods ensure the continuation can only be used once.

To create a continuation call [`withContinuation(of:throwing:_:)`](./withcontinuation%28of,throwing,_%29.md).

To resume the task, suspended on a continuation, call [`resume(returning:)`](./continuation/resume%28returning%29-5fa8w.md), [`resume(throwing:)`](./continuation/resume%28throwing%29.md), [`resume(with:)`](./continuation/resume%28with%29.md), or [`resume()`](./continuation/resume%28%29.md).

> **See Also**: [`CheckedContinuation`](./checkedcontinuation.md)

## Topics

### Instance Methods
- [func resume()](./continuation/resume%28%29.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(returning: consuming sending Success)](./continuation/resume%28returning%29-5fa8w.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(returning: consuming sending Success)](./continuation/resume%28returning%29-8uw9b.md)
  Resume the task awaiting the continuation by having it return from its suspension point
- [func resume(throwing: Failure)](./continuation/resume%28throwing%29.md)
  Resume the task awaiting the continuation by having it throw an error from its suspension point
- [func resume(with: consuming sending Result<Success, Failure>)](./continuation/resume%28with%29.md)
  Resume the task awaiting the continuation by having it either return or throw an error based on the state of the given `Result` value

## Relationships

### Conforms To
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)

## See Also

### Continuations
- [func withContinuation<Success>(of: Success.Type, (consuming Continuation<Success, Never>) -> Void) async -> sending Success](./withcontinuation%28of,_%29.md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [func withContinuation<Success, Failure>(of: Success.Type, throwing: Failure.Type, (consuming Continuation<Success, Failure>) -> Void) async throws(Failure) -> sending Success](./withcontinuation%28of,throwing,_%29.md)
  Invokes the passed in closure with a non-copyable continuation for the current task.
- [struct CheckedContinuation](./checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](./withcheckedcontinuation%28function,_%29.md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](./withcheckedthrowingcontinuation%28function,_%29-13yf6.md)
- [func withCheckedThrowingContinuation<T, E>(function: String, (CheckedContinuation<T, E>) -> Void) async throws(E) -> sending T](./withcheckedthrowingcontinuation%28function,_%29-2k46m.md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](./unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>((UnsafeContinuation<T, Never>) -> Void) async -> sending T](./withunsafecontinuation%28_%29.md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [func withUnsafeThrowingContinuation<T, E>((UnsafeContinuation<T, E>) -> Void) async throws(E) -> sending T](./withunsafethrowingcontinuation%28_%29-32nwt.md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [func withUnsafeThrowingContinuation<T>((UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](./withunsafethrowingcontinuation%28_%29-7zhvy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuation)*