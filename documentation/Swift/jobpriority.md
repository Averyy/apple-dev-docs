# JobPriority

**Framework**: Swift  
**Kind**: struct

The priority of this job.

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
struct JobPriority
```

#### Overview

The executor determines how priority information affects the way tasks are scheduled. The behavior varies depending on the executor currently being used. Typically, executors attempt to run tasks with a higher priority before tasks with a lower priority. However, the semantics of how priority is treated are left up to each platform and `Executor` implementation.

A ExecutorJob’s priority is roughly equivalent to a `TaskPriority`, however, since not all jobs are tasks, represented as separate type.

Conversions between the two priorities are available as initializers on the respective types.

## Topics

### Operators
- [static func != (JobPriority, JobPriority) -> Bool](jobpriority/!=(_:_:).md)
### Instance Properties
- [var rawValue: JobPriority.RawValue](jobpriority/rawvalue-swift.property.md)
  The raw priority value.
### Type Aliases
- [JobPriority.RawValue](jobpriority/rawvalue-swift.typealias.md)
### Default Implementations
- [Comparable Implementations](jobpriority/comparable-implementations.md)
- [Equatable Implementations](jobpriority/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
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
- [struct UnownedSerialExecutor](unownedserialexecutor.md)
  An unowned reference to a serial executor (a `SerialExecutor` value).
- [struct UnownedTaskExecutor](unownedtaskexecutor.md)
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/jobpriority)*