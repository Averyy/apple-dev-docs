# Executor

**Framework**: Swift  
**Kind**: protocol

A service that can execute jobs.

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
protocol Executor : AnyObject, Sendable
```

## Topics

### Instance Properties
- [var isMainExecutor: Bool](executor/ismainexecutor.md)
  `true` if this is the main executor.
### Instance Methods
- [func enqueue(consuming Job)](executor/enqueue(_:)-2sc5t.md)
- [func enqueue(consuming ExecutorJob)](executor/enqueue(_:)-55qpq.md)
- [func enqueue(UnownedJob)](executor/enqueue(_:)-b90u.md)

## Relationships

### Inherits From
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
### Inherited By
- [MainExecutor](mainexecutor.md)
- [RunLoopExecutor](runloopexecutor.md)
- [SchedulableExecutor](schedulableexecutor.md)
- [SerialExecutor](serialexecutor.md)
- [TaskExecutor](taskexecutor.md)
### Conforming Types
- [CFMainExecutor](cfmainexecutor.md)
- [CFTaskExecutor](cftaskexecutor.md)
- [DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [DispatchMainExecutor](dispatchmainexecutor.md)
- [DummyMainExecutor](dummymainexecutor.md)
- [DummyTaskExecutor](dummytaskexecutor.md)

## See Also

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
- [struct UnownedTaskExecutor](unownedtaskexecutor.md)
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executor)*