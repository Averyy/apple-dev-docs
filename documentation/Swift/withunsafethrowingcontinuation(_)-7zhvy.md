# withUnsafeThrowingContinuation(_:)

**Framework**: Swift  
**Kind**: func  
**Role**: Function

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
nonisolated
(nonsending) func withUnsafeThrowingContinuation<T>(_ fn: (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T
```

## See Also

### Continuations
- [struct Continuation](./continuation.md)
  A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafethrowingcontinuation(_:)-7zhvy)*