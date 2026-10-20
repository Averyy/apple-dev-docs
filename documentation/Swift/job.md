# Job

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Deprecated equivalent of [`ExecutorJob`](./executorjob.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
struct Job
```

#### Overview

A unit of schedulable work.

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

## Topics

### Initializers
- [init(UnownedJob)](./job/init%28_%29-6f0eq.md)
- [init(ExecutorJob)](./job/init%28_%29-6pzn2.md)
### Instance Properties
- [var description: String](./job/description.md)
- [var priority: JobPriority](./job/priority.md)
### Instance Methods
- [func runSynchronously(on: UnownedSerialExecutor)](./job/runsynchronously%28on%29.md)
  Run this job on the passed in executor.

## Relationships

### Conforms To
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
- [typealias PartialAsyncTask](./partialasynctask.md)
- [typealias UnsafeConcurrentValue](./unsafeconcurrentvalue.md)
- [protocol UnsafeSendable](./unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeThrowingContinuation](./unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](./withunsafethrowingcontinuation%28isolation,_%29.md)
  Source-compatibility overload; replaced by [`withUnsafeThrowingContinuation(_:)`](./withunsafethrowingcontinuation%28_%29-32nwt.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/job)*