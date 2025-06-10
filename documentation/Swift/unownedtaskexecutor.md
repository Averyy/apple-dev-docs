# UnownedTaskExecutor

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct UnownedTaskExecutor
```

## Topics

### Initializers
- [init(Builtin.Executor)](unownedtaskexecutor/init(_:)-55b8h.md)
- [init<E>(E)](unownedtaskexecutor/init(_:)-5pjm5.md)
- [init<E>(ordinary: E)](unownedtaskexecutor/init(ordinary:).md)
### Instance Methods
- [func asTaskExecutor() -> (any TaskExecutor)?](unownedtaskexecutor/astaskexecutor.md)
### Default Implementations
- [Equatable Implementations](unownedtaskexecutor/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
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
- [struct JobPriority](jobpriority.md)
  The priority of this job.
- [struct UnownedSerialExecutor](unownedserialexecutor.md)
  An unowned reference to a serial executor (a `SerialExecutor` value).
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedtaskexecutor)*