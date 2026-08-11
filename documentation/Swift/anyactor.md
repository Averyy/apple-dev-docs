# AnyActor

**Framework**: Swift  
**Kind**: typealias

Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.

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
typealias AnyActor = AnyObject & Sendable
```

#### Discussion

The `AnyActor` marker protocol generalizes over all actor types, including distributed ones. In practice, this protocol can be used to restrict protocols, or generic parameters to only be usable with actors, which provides the guarantee that calls may be safely made on instances of given type without worrying about the thread-safety of it – as they are guaranteed to follow the actor-style isolation semantics.

While both local and distributed actors are conceptually “actors”, there are some important isolation model differences between the two, which make it impossible for one to refine the other.

## See Also

- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by [`withCheckedContinuation(function:_:)`](withcheckedcontinuation(function:_:).md).
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by [`withCheckedThrowingContinuation(function:_:)`](withcheckedthrowingcontinuation(function:_:)-2k46m.md).
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by [`withUnsafeContinuation(_:)`](withunsafecontinuation(_:).md).
- [typealias ConcurrentValue](concurrentvalue.md)
- [struct Job](job.md)
  Deprecated equivalent of [`ExecutorJob`](executorjob.md).
- [typealias PartialAsyncTask](partialasynctask.md)
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T, E>((UnsafeContinuation<T, E>) -> Void) async throws(E) -> sending T](withunsafethrowingcontinuation(_:)-32nwt.md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [func withUnsafeThrowingContinuation<T>((UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(_:)-7zhvy.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by [`withUnsafeThrowingContinuation(_:)`](withunsafethrowingcontinuation(_:)-32nwt.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyactor)*