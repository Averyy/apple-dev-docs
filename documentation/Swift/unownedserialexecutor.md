# UnownedSerialExecutor

**Framework**: Swift  
**Kind**: struct

An unowned reference to a serial executor (a `SerialExecutor` value).

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
struct UnownedSerialExecutor
```

#### Overview

This is an optimized type used internally by the core scheduling operations.  It is an unowned reference to avoid unnecessary reference-counting work even when working with actors abstractly. Generally there are extra constraints imposed on core operations in order to allow this.  For example, keeping an actor alive must also keep the actor’s associated executor alive; if they are different objects, the executor must be referenced strongly by the actor.

## Topics

### Initializers
- [init(Builtin.Executor)](unownedserialexecutor/init(_:)-8mpaa.md)
- [init<E>(E)](unownedserialexecutor/init(_:)-9jcxo.md)
  Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.
- [init<E>(complexEquality: E)](unownedserialexecutor/init(complexequality:).md)
  Opts the executor into complex “same exclusive execution context” equality checks.
- [init<E>(ordinary: E)](unownedserialexecutor/init(ordinary:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol Executor](executor.md)
  A service that can execute jobs.
- [struct ExecutorJob](executorjob.md)
  A unit of schedulable work.
- [protocol SerialExecutor](serialexecutor.md)
  A service that executes jobs.
- [protocol TaskExecutor](taskexecutor.md)
  An executor that may be used as preferred executor by a task.
- [typealias PartialAsyncTask](partialasynctask.md)
- [struct UnownedJob](unownedjob.md)
  A unit of schedulable work.
- [struct JobPriority](jobpriority.md)
  The priority of this job.
- [struct UnownedTaskExecutor](unownedtaskexecutor.md)
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedserialexecutor)*