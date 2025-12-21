# ThrowingDiscardingTaskGroup

**Framework**: Swift  
**Kind**: struct

A throwing discarding group that contains dynamically created child tasks.

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
struct ThrowingDiscardingTaskGroup<Failure> where Failure : Error
```

#### Overview

To create a discarding task group, call the `withDiscardingTaskGroup(returning:body:)` method.

Don’t use a task group from outside the task where you created it. In most cases, the Swift type system prevents a task group from escaping like that because adding a child task to a task group is a mutating operation, and mutation operations can’t be performed from a concurrent execution context like a child task.

Refer to [`TaskGroup`](taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

##### Discarding Behavior

A discarding task group eagerly discards and releases its child tasks as soon as they complete. This allows for the efficient releasing of memory used by those tasks, which are not retained for future `next()` calls, as would be the case with a [`TaskGroup`](taskgroup.md).

##### Cancellation Behavior

A throwing discarding task group becomes canceled in one of the following ways:

- when [`cancelAll()`](throwingdiscardingtaskgroup/cancelall().md) is invoked on it,
- when an error is thrown out of the `withThrowingDiscardingTaskGroup { ... }` closure,
- when the [`Task`](task.md) running this task group is canceled.

But also, and uniquely in  task groups:

- when  of its child tasks throws.

The group becoming canceled automatically, and cancelling all of its child tasks, whenever  child task throws an error is a behavior unique to discarding task groups, because achieving such semantics is not possible otherwise, due to the missing `next()` method on discarding groups. Accumulating task groups can implement this by manually polling `next()` and deciding to `cancelAll()` when they decide an error should cause the group to become canceled, however a discarding group cannot poll child tasks for results and therefore assumes that child task throws are an indication of a group wide failure. In order to avoid such behavior, use a [`DiscardingTaskGroup`](discardingtaskgroup.md) instead of a throwing one, or catch specific errors in operations submitted using `addTask`.

Since a `ThrowingDiscardingTaskGroup` is a structured concurrency primitive, cancellation is automatically propagated through all of its child-tasks (and their child tasks).

A canceled task group can still keep adding tasks, however they will start being immediately canceled, and may act accordingly to this. To avoid adding new tasks to an already canceled task group, use `addTaskUnlessCancelled(priority:body:)` rather than the plain `addTask(priority:body:)` which adds tasks unconditionally.

For information about the language-level concurrency model that `DiscardingTaskGroup` is part of, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

> **Note**: [`TaskGroup`](taskgroup.md)

> **Note**: [`ThrowingTaskGroup`](throwingtaskgroup.md)

> **Note**: [`DiscardingTaskGroup`](discardingtaskgroup.md)

## Topics

### Instance Properties
- [var isCancelled: Bool](throwingdiscardingtaskgroup/iscancelled.md)
  A Boolean value that indicates whether the group was canceled.
- [var isEmpty: Bool](throwingdiscardingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
### Instance Methods
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> Void)](throwingdiscardingtaskgroup/addimmediatetask(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> Void) -> Bool](throwingdiscardingtaskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Void)](throwingdiscardingtaskgroup/addtask(executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Void)](throwingdiscardingtaskgroup/addtask(name:executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async throws -> Void)](throwingdiscardingtaskgroup/addtask(name:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(priority: TaskPriority?, operation: sending () async throws -> Void)](throwingdiscardingtaskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Void) -> Bool](throwingdiscardingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Void) -> Bool](throwingdiscardingtaskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async throws -> Void) -> Bool](throwingdiscardingtaskgroup/addtaskunlesscancelled(name:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async throws -> Void) -> Bool](throwingdiscardingtaskgroup/addtaskunlesscancelled(priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func cancelAll()](throwingdiscardingtaskgroup/cancelall.md)
  Cancel all of the remaining tasks in the group.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)

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
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](withthrowingdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct UnsafeCurrentTask](unsafecurrenttask.md)
  An unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup)*