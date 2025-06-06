# globalConcurrentExecutor

**Framework**: Swift  
**Kind**: var

The global concurrent executor that is used by default for Swift Concurrency tasks.

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
var globalConcurrentExecutor: any TaskExecutor { get }
```

#### Discussion

The executor’s implementation is platform dependent. By default it uses a fixed size pool of threads and should not be used for blocking operations which do not guarantee forward progress as doing so may prevent other tasks from being executed and render the system unresponsive.

You may pass this executor explicitly to a [`Task`](task.md) initializer as a task executor preference, in order to ensure and document that task be executed on the global executor, instead e.g. inheriting the enclosing actor’s executor. Refer to `withTaskExecutorPreference(_:operation:)` for a detailed discussion of task executor preferences.

Customizing the global concurrent executor is currently not supported.

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
- [struct UnownedTaskExecutor](unownedtaskexecutor.md)
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/globalconcurrentexecutor)*