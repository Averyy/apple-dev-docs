# immediateDetached(name:priority:executorPreference:operation:)

**Framework**: Swift  
**Kind**: method

Create and immediately start running a new task in the context of the calling thread/task.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@discardableResult
static func immediateDetached(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async throws -> Success) -> Task<Success, any Error>
```

#### Return Value

A reference to the unstructured task which may be awaited on.

#### Discussion

This function  the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does  suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to a task created using the `Task/detached` function.

## Parameters

- `name`: The high-level human-readable name given for this task
- `priority`: The priority of the task.   Pass   to use the   of the current task (if there is one).
- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to no preference,   and effectively means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `operation`: The operation to be run immediately upon entering the task.

## See Also

- [static func immediate(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> Success) -> Task<Success, Never>](task/immediate(name:priority:executorpreference:operation:)-88o80.md)
  Create and immediately start running a new detached task in the context of the calling thread/task.
- [static func immediate(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> Success) -> Task<Success, any Error>](task/immediate(name:priority:executorpreference:operation:)-9bghc.md)
  Create and immediately start running a new detached task in the context of the calling thread/task.
- [static func immediateDetached(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> Success) -> Task<Success, Never>](task/immediatedetached(name:priority:executorpreference:operation:)-7h41b.md)
  Create and immediately start running a new task in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/immediatedetached(name:priority:executorpreference:operation:)-52ipd)*