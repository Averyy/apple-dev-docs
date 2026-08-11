# withUnsafeThrowingContinuation(_:)

**Framework**: Swift  
**Kind**: func

Invokes the passed in closure with a unsafe continuation for the current task.

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
(nonsending) func withUnsafeThrowingContinuation<T, E>(_ fn: (UnsafeContinuation<T, E>) -> Void) async throws(E) -> sending T where E : Error
```

#### Return Value

The value continuation is resumed with.

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

If `resume(throwing:)` is called on the continuation, this function throws that error.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

Unlike the “checked” continuation variant, the `UnsafeContinuation` does not detect or diagnose any kind of misuse, so you need to be extra careful to avoid calling `resume` twice or forgetting to call resume before letting go of the continuation object.

> **Note**: `withUnsafeContinuation(function:_:)`

> **Note**: `withCheckedContinuation(function:_:)`

> **Note**: `withCheckedThrowingContinuation(function:_:)`

## Parameters

- `fn`: A closure that takes an `UnsafeContinuation` parameter.

## See Also

- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by [`withCheckedContinuation(function:_:)`](withcheckedcontinuation(function:_:).md).
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by [`withCheckedThrowingContinuation(function:_:)`](withcheckedthrowingcontinuation(function:_:)-2k46m.md).
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by [`withUnsafeContinuation(_:)`](withunsafecontinuation(_:).md).
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [typealias ConcurrentValue](concurrentvalue.md)
- [struct Job](job.md)
  Deprecated equivalent of [`ExecutorJob`](executorjob.md).
- [typealias PartialAsyncTask](partialasynctask.md)
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>((UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(_:)-7zhvy.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by [`withUnsafeThrowingContinuation(_:)`](withunsafethrowingcontinuation(_:)-32nwt.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafethrowingcontinuation(_:)-32nwt)*