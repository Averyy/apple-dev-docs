# UnsafeCurrentTask

**Framework**: Swift  
**Kind**: struct

An unsafe reference to the current task.

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
struct UnsafeCurrentTask
```

#### Overview

To get an instance of `UnsafeCurrentTask` for the current task, call the `withUnsafeCurrentTask(body:)` method. Don’t store an unsafe task reference for use outside that method’s closure. Storing an unsafe reference doesn’t affect the task’s actual life cycle, and the behavior of accessing an unsafe task reference outside of the `withUnsafeCurrentTask(body:)` method’s closure isn’t defined.

Only APIs on `UnsafeCurrentTask` that are also part of `Task` are safe to invoke from a task other than the task that this `UnsafeCurrentTask` instance refers to. Calling other APIs from another task is undefined behavior, breaks invariants in other parts of the program running on this task, and may lead to crashes or data loss.

For information about the language-level concurrency model that `UnsafeCurrentTask` is part of, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

## Topics

### Getting an Unsafe Reference to the Current Task
- [func withUnsafeCurrentTask<T>(body: (UnsafeCurrentTask?) throws -> T) rethrows -> T](withunsafecurrenttask(body:)-6gvhl.md)
  Calls a closure with an unsafe reference to the current task.
- [func withUnsafeCurrentTask<T>(body: nonisolated(nonsending) (UnsafeCurrentTask?) async throws -> T) async rethrows -> T](withunsafecurrenttask(body:)-udlb.md)
  Calls a closure with an unsafe reference to the current task.
### Instance Properties
- [var basePriority: TaskPriority](unsafecurrenttask/basepriority.md)
  The current task’s base priority.
- [var hasActiveCancellationShield: Bool](unsafecurrenttask/hasactivecancellationshield.md)
  Checks if this task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)-(()->Value)` function.
- [var isCancelled: Bool](unsafecurrenttask/iscancelled.md)
  A Boolean value that indicates whether the current task was canceled.
- [var name: String?](unsafecurrenttask/name.md)
  Return the task’s name, if it was set during its creation.
- [var priority: TaskPriority](unsafecurrenttask/priority.md)
  The current task’s priority.
- [var unownedTaskExecutor: UnownedTaskExecutor?](unsafecurrenttask/unownedtaskexecutor.md)
  The current [`TaskExecutor`](taskexecutor.md) preference, if this task has one configured.
### Instance Methods
- [func cancel()](unsafecurrenttask/cancel.md)
  Cancel the current task.
- [func escalatePriority(to: TaskPriority)](unsafecurrenttask/escalatepriority(to:).md)
  Escalate the task `priority` of the passed in task to the `newPriority`.
### Default Implementations
- [Equatable Implementations](unsafecurrenttask/equatable-implementations.md)
- [Hashable Implementations](unsafecurrenttask/hashable-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [struct Task](task.md)
  A unit of asynchronous work.
- [struct TaskGroup](taskgroup.md)
  A group that contains dynamically created child tasks.
- [func withTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout TaskGroup<ChildTaskResult>) async -> GroupResult) async -> GroupResult](withtaskgroup(of:returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct ThrowingTaskGroup](throwingtaskgroup.md)
  A group that contains throwing, dynamically created child tasks.
- [func withThrowingTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingTaskGroup<ChildTaskResult, any Error>) async throws -> GroupResult) async rethrows -> GroupResult](withthrowingtaskgroup(of:returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of throwing child tasks.
- [struct TaskPriority](taskpriority.md)
  The priority of a task.
- [struct DiscardingTaskGroup](discardingtaskgroup.md)
  A discarding group that contains dynamically created child tasks.
- [func withDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout DiscardingTaskGroup) async -> GroupResult) async -> GroupResult](withdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md)
  A throwing discarding group that contains dynamically created child tasks.
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](withthrowingdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask)*