# withTaskExecutorPreference(_:isolation:operation:)

**Framework**: Swift  
**Kind**: func

Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.

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
func withTaskExecutorPreference<T, Failure>(_ taskExecutor: (any TaskExecutor)?, isolation: isolated (any Actor)? = #isolation, operation: () async throws(Failure) -> T) async throws(Failure) -> T where Failure : Error
```

#### Return Value

The value returned from the `operation` closure

##### Task Executor Preference Semantics

Task executors influence  nonisolated asynchronous functions, and default actor methods execute. The preferred executor will be used whenever possible, rather than hopping to the global concurrent pool.

For an in depth discussion of this topic, see [`TaskExecutor`](taskexecutor.md).

##### Disabling Task Executor Preference

Passing `nil` as executor means disabling any preference preference (if it was set) and the task hierarchy will execute without any executor preference until a different preference is set.

##### Asynchronous Function Execution Semantics in Presence of Task Executor Preferences

The following diagram illustrates on which executor an `async` function will execute, in presence (or lack thereof) a task executor preference.

```swift
[ func / closure ] - /* where should it execute? */
                              |
                    +--------------+          +===========================+
          +-------- | is isolated? | - yes -> | actor has unownedExecutor |
          |         +--------------+          +===========================+
          |                                       |                |
          |                                      yes               no
          |                                       |                |
          |                                       v                v
          |                  +=======================+    /* task executor preference? */
          |                  | on specified executor |        |                   |
          |                  +=======================+       yes                  no
          |                                                   |                   |
          |                                                   |                   v
          |                                                   |    +==========================+
          |                                                   |    | default (actor) executor |
          |                                                   v    +==========================+
          v                                     +==============================+
 /* task executor preference? */ ---- yes ----> | on Task's preferred executor |
          |                                     +==============================+
          no
          |
          v
 +===============================+
 | on global concurrent executor |
 +===============================+
```

In short, without a task executor preference, `nonisolated async` functions will execute on the global concurrent executor. If a task executor preference is present, such `nonisolated async` functions will execute on the preferred task executor.

Isolated functions semantically execute on the actor they are isolated to, however if such actor does not declare a custom executor (it is a “default actor”) in presence of a task executor preference, tasks executing on this actor will use the preferred executor as source of threads to run the task, while isolated on the actor.

##### Example

```swift
Task {
  // case 0) "no task executor preference"

  // default task executor
  // ...
  await SomeDefaultActor().hello() // default executor
  await ActorWithCustomExecutor().hello() // 'hello' executes on actor's custom executor

  // child tasks execute on default executor:
  async let x = ...
  await withTaskGroup(of: Int.self) { group in g.addTask { 7 } }

  await withTaskExecutorPreference(specific) {
    // case 1) 'specific' task executor preference

    // 'specific' task executor
    // ...
    await SomeDefaultActor().hello() // 'hello' executes on 'specific' executor
    await ActorWithCustomExecutor().hello() // 'hello' executes on actor's custom executor (same as case 0)

    // child tasks execute on 'specific' task executor:
    async let x = ...
    await withTaskGroup(of: Int.self) { group in
      group.addTask { 7 } // child task executes on 'specific' executor
      group.addTask(executorPreference: globalConcurrentExecutor) { 13 } // child task executes on global concurrent executor
    }

    // disable the task executor preference:
    await withTaskExecutorPreference(globalConcurrentExecutor) {
      // equivalent to case 0) preference is globalConcurrentExecutor

      // default task executor
      // ...
      await SomeDefaultActor().hello() // default executor (same as case 0)
      await ActorWithCustomExecutor().hello() // 'hello' executes on actor's custom executor (same as case 0)

      // child tasks execute on default executor (same as case 0):
      async let x = ...
      await withTaskGroup(of: Int.self) { group in group.addTask { 7 } }
    }
  }
}
```

> **Note**: If the operation closure throws

> **Note**: [`TaskExecutor`](taskexecutor.md)

## Parameters

- `taskExecutor`: The executor to use as preferred task executor for this   operation, and any child tasks created inside the   closure.   If   it is interpreted as “no preference” and calling this method   will have no impact on execution semantics of the 
- `operation`: The operation to execute on the passed executor

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
- [var globalConcurrentExecutor: any TaskExecutor](globalconcurrentexecutor.md)
  The global concurrent executor that is used by default for Swift Concurrency tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtaskexecutorpreference(_:isolation:operation:))*