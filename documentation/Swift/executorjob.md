# ExecutorJob

**Framework**: Swift  
**Kind**: struct

A unit of schedulable work.

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
struct ExecutorJob
```

#### Overview

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

## Topics

### Initializers
- [init(Job)](executorjob/init(_:)-2yixs.md)
- [init(UnownedJob)](executorjob/init(_:)-36632.md)
### Instance Properties
- [var description: String](executorjob/description.md)
- [var priority: JobPriority](executorjob/priority.md)
### Instance Methods
- [func runSynchronously(isolatedTo: UnownedSerialExecutor, taskExecutor: UnownedTaskExecutor)](executorjob/runsynchronously(isolatedto:taskexecutor:).md)
  Run this job isolated to the passed in serial executor, while executing it on the specified task executor.
- [func runSynchronously(on: UnownedTaskExecutor)](executorjob/runsynchronously(on:)-6e565.md)
  Run this job on the passed in task executor.
- [func runSynchronously(on: UnownedSerialExecutor)](executorjob/runsynchronously(on:)-9dhs1.md)
  Run this job on the passed in executor.

## Relationships

### Conforms To
- [Sendable](sendable.md)

## See Also

- [protocol Executor](executor.md)
  A service that can execute jobs.
- [protocol SerialExecutor](serialexecutor.md)
  A service that executes jobs.
- [protocol TaskExecutor](taskexecutor.md)
  An executor that may be used as preferred executor by a task.
- [typealias PartialAsyncTask](partialasynctask.md)
- [struct UnownedJob](unownedjob.md)
  A unit of schedulable work.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob)*