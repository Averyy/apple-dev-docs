# PartialAsyncTask

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

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
typealias PartialAsyncTask = UnownedJob
```

## See Also

### Deprecated
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](./extractisolation%28_%29.md)
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](./withcheckedcontinuation%28isolation,function,_%29.md)
  Source-compatibility overload; replaced by [`withCheckedContinuation(function:_:)`](./withcheckedcontinuation%28function,_%29.md).
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](./withcheckedthrowingcontinuation%28isolation,function,_%29.md)
  Source-compatibility overload; replaced by [`withCheckedThrowingContinuation(function:_:)`](./withcheckedthrowingcontinuation%28function,_%29-2k46m.md).
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](./withunsafecontinuation%28isolation,_%29.md)
  Source-compatibility overload; replaced by [`withUnsafeContinuation(_:)`](./withunsafecontinuation%28_%29.md).
- [typealias AnyActor](./anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [typealias ConcurrentValue](./concurrentvalue.md)
- [struct Job](./job.md)
  Deprecated equivalent of [`ExecutorJob`](./executorjob.md).
- [typealias UnsafeConcurrentValue](./unsafeconcurrentvalue.md)
- [protocol UnsafeSendable](./unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeThrowingContinuation](./unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](./withunsafethrowingcontinuation%28isolation,_%29.md)
  Source-compatibility overload; replaced by [`withUnsafeThrowingContinuation(_:)`](./withunsafethrowingcontinuation%28_%29-32nwt.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialasynctask)*