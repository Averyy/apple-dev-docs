# TaskExecutor

**Framework**: Swift  
**Kind**: protocol

An executor that may be used as preferred executor by a task.

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
protocol TaskExecutor : Executor
```

##### Impact of Setting a Task Executor Preference

By default, without setting a task executor preference, nonisolated asynchronous functions, as well as methods declared on default actors – that is actors which do not require a specific executor – execute on Swift’s default global concurrent executor. This is an executor shared by the entire runtime to execute any work which does not have strict executor requirements.

By setting a task executor preference, either with a `withTaskExecutorPreference(_:operation:)`, creating a task with a preference (`Task(executorPreference:)`, or `group.addTask(executorPreference:)`), the task and all of its child tasks (unless a new preference is set) will be preferring to execute on the provided task executor.

Unstructured tasks do not inherit the task executor.

## Topics

### Instance Methods
- [func asUnownedTaskExecutor() -> UnownedTaskExecutor](taskexecutor/asunownedtaskexecutor.md)
- [func enqueue(consuming ExecutorJob)](taskexecutor/enqueue(_:)-30ge1.md)
- [func enqueue(consuming Job)](taskexecutor/enqueue(_:)-6vkr9.md)
- [func enqueue(UnownedJob)](taskexecutor/enqueue(_:)-91eir.md)

## Relationships

### Inherits From
- [Executor](executor.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol Executor](executor.md)
  A service that can execute jobs.
- [struct ExecutorJob](executorjob.md)
  A unit of schedulable work.
- [protocol SerialExecutor](serialexecutor.md)
  A service that executes jobs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskexecutor)*