# withCheckedThrowingContinuation(function:_:)

**Framework**: Swift  
**Kind**: func

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
@abi(nonisolated(nonsending) func withCheckedThrowingContinuationNonisolatedNonsending<T>(function: String, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T) nonisolated(nonsending) func withCheckedThrowingContinuation<T>(function: String = #function, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T
```

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
- [func withCheckedThrowingContinuation<T, E>(function: String, (CheckedContinuation<T, E>) -> Void) async throws(E) -> sending T](withcheckedthrowingcontinuation(function:_:)-2k46m.md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>((UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcheckedthrowingcontinuation(function:_:)-13yf6)*