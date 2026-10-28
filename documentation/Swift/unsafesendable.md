# UnsafeSendable

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use @unchecked Sendable instead

## Declaration

```swift
protocol UnsafeSendable : Sendable
```

## Overview

Use an unchecked conformance to `Sendable` instead — for example:

```swift
struct MyStructure: @unchecked Sendable { ... }
```

## Relationships

### Inherits From
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)

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
- [typealias PartialAsyncTask](./partialasynctask.md)
- [typealias UnsafeConcurrentValue](./unsafeconcurrentvalue.md)
- [typealias UnsafeThrowingContinuation](./unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](./withunsafethrowingcontinuation%28isolation,_%29.md)
  Source-compatibility overload; replaced by [`withUnsafeThrowingContinuation(_:)`](./withunsafethrowingcontinuation%28_%29-32nwt.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafesendable)*