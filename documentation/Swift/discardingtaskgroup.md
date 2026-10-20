# DiscardingTaskGroup

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A discarding group that contains dynamically created child tasks.

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
struct DiscardingTaskGroup
```

#### Overview

To create a discarding task group, call the [`withDiscardingTaskGroup(returning:isolation:body:)`](./withdiscardingtaskgroup%28returning,isolation,body%29.md) method.

Don’t use a task group from outside the task where you created it. In most cases, the Swift type system prevents a task group from escaping like that because adding a child task to a task group is a mutating operation, and mutation operations can’t be performed from a concurrent execution context like a child task.

Refer to [`TaskGroup`](./taskgroup.md) documentation for detailed discussion of semantics shared between all task groups.

##### Discarding behavior

A discarding task group eagerly discards and releases its child tasks as soon as they complete. This allows for the efficient releasing of memory used by those tasks, which are not retained for future `next()` calls, as would be the case with a [`TaskGroup`](./taskgroup.md).

##### Cancellation behavior

A discarding task group becomes canceled in one of the following ways:

- when [`cancelAll()`](./discardingtaskgroup/cancelall%28%29.md) is invoked on it,
- when the [`Task`](./task.md) running this task group is canceled.

Since a `DiscardingTaskGroup` is a structured concurrency primitive, cancellation is automatically propagated through all of its child-tasks (and their child tasks).

A canceled task group can still keep adding tasks, however they will start being immediately canceled, and may act accordingly to this. To avoid adding new tasks to an already canceled task group, use [`addTaskUnlessCancelled(priority:operation:)`](./discardingtaskgroup/addtaskunlesscancelled%28priority,operation%29.md) rather than the plain [`addTask(priority:operation:)`](./discardingtaskgroup/addtask%28priority,operation%29.md) which adds tasks unconditionally.

For information about the language-level concurrency model that `DiscardingTaskGroup` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

> **See Also**: [`TaskGroup`](./taskgroup.md)

> **See Also**: [`ThrowingTaskGroup`](./throwingtaskgroup.md)

> **See Also**: [`ThrowingDiscardingTaskGroup`](./throwingdiscardingtaskgroup.md)

## Topics

### Instance Properties
- [var isCancelled: Bool](./discardingtaskgroup/iscancelled.md)
  A Boolean value that indicates whether the group was canceled.
- [var isEmpty: Bool](./discardingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
### Instance Methods
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> Void)](./discardingtaskgroup/addimmediatetask%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> Void) -> Bool](./discardingtaskgroup/addimmediatetaskunlesscancelled%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Void)](./discardingtaskgroup/addtask%28executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Void)](./discardingtaskgroup/addtask%28name,executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async -> Void)](./discardingtaskgroup/addtask%28name,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(priority: TaskPriority?, operation: sending () async -> Void)](./discardingtaskgroup/addtask%28priority,operation%29.md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Void) -> Bool](./discardingtaskgroup/addtaskunlesscancelled%28executorpreference,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Void) -> Bool](./discardingtaskgroup/addtaskunlesscancelled%28name,executorpreference,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async -> Void) -> Bool](./discardingtaskgroup/addtaskunlesscancelled%28name,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async -> Void) -> Bool](./discardingtaskgroup/addtaskunlesscancelled%28priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func cancelAll()](./discardingtaskgroup/cancelall%28%29.md)
  Cancel all of the remaining tasks in the group.

## Relationships

### Conforms To
- [BitwiseCopyable](./bitwisecopyable.md)
- [Copyable](./copyable.md)

## See Also

### Tasks
- [struct Task](./task.md)
  A unit of asynchronous work.
- [struct TaskGroup](./taskgroup.md)
  A group that contains dynamically created child tasks.
- [func withTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout TaskGroup<ChildTaskResult>) async -> GroupResult) async -> GroupResult](./withtaskgroup%28of,returning,isolation,body%29.md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct ThrowingTaskGroup](./throwingtaskgroup.md)
  A group that contains throwing, dynamically created child tasks.
- [func withThrowingTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingTaskGroup<ChildTaskResult, any Error>) async throws -> GroupResult) async rethrows -> GroupResult](./withthrowingtaskgroup%28of,returning,isolation,body%29.md)
  Starts a new scope that can contain a dynamic number of throwing child tasks.
- [struct TaskPriority](./taskpriority.md)
  The priority of a task.
- [func withDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout DiscardingTaskGroup) async -> GroupResult) async -> GroupResult](./withdiscardingtaskgroup%28returning,isolation,body%29.md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct ThrowingDiscardingTaskGroup](./throwingdiscardingtaskgroup.md)
  A throwing discarding group that contains dynamically created child tasks.
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](./withthrowingdiscardingtaskgroup%28returning,isolation,body%29.md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct UnsafeCurrentTask](./unsafecurrenttask.md)
  An unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discardingtaskgroup)*