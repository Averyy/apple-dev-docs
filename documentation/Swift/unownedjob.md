# UnownedJob

**Framework**: Swift  
**Kind**: struct

A unit of schedulable work.

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
struct UnownedJob
```

#### Overview

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

An `UnownedJob` must be eventually run  using `runSynchronously(on:)`. Not doing so is effectively going to leak and “hang” the work that the job represents (e.g. a [`Task`](task.md)).

## Topics

### Initializers
- [init(ExecutorJob)](unownedjob/init(_:)-8ra8c.md)
  Create an `UnownedJob` whose lifetime must be managed carefully until it is run exactly once.
- [init(Job)](unownedjob/init(_:)-9f1zn.md)
  Create an `UnownedJob` whose lifetime must be managed carefully until it is run exactly once.
### Instance Properties
- [var priority: JobPriority](unownedjob/priority.md)
  The priority of this job.
### Instance Methods
- [func runSynchronously(isolatedTo: UnownedSerialExecutor, taskExecutor: UnownedTaskExecutor)](unownedjob/runsynchronously(isolatedto:taskexecutor:).md)
  Run this job isolated to the passed in serial executor, while executing it on the specified task executor.
- [func runSynchronously(on: UnownedTaskExecutor)](unownedjob/runsynchronously(on:)-4eaxu.md)
  Run this job isolated to the passed task executor.
- [func runSynchronously(on: UnownedSerialExecutor)](unownedjob/runsynchronously(on:)-o1nb.md)
  Run this job on the passed in executor.
### Default Implementations
- [CustomStringConvertible Implementations](unownedjob/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
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
- [struct JobPriority](jobpriority.md)
  The priority of this job.
- [struct UnownedSerialExecutor](unownedserialexecutor.md)
  An unowned reference to a serial executor (a `SerialExecutor` value).
- [struct UnownedTaskExecutor](unownedtaskexecutor.md)
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedjob)*