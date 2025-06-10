# withThrowingDiscardingTaskGroup(returning:isolation:body:)

**Framework**: Swift  
**Kind**: func

Starts a new scope that can contain a dynamic number of child tasks.

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
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withThrowingDiscardingTaskGroup<GroupResult>(returning returnType: GroupResult.Type = GroupResult.self, isolation: isolated (any Actor)? = #isolation, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult
```

#### Discussion

Unlike a [`ThrowingTaskGroup`](throwingtaskgroup.md), the child tasks as well as their results are discarded as soon as the tasks complete. This prevents the discarding task group from accumulating many results waiting to be consumed, and is best applied in situations where the result of a child task is some form of side-effect.

A group waits for all of its child tasks to complete before it returns. Even cancelled tasks must run until completion before this function returns. Cancelled child tasks cooperatively react to cancellation and attempt to return as early as possible. After this function returns, the task group is always empty.

It is not possible to explicitly await completion of child-tasks, however the group will automatically await  child task completions before returning from this function:

```swift
try await withThrowingDiscardingTaskGroup(of: Void.self) { group in
  group.addTask { /* slow-task */ }
  // slow-task executes...
}
// guaranteed that slow-task has completed and the group is empty & destroyed
```

### Task Group Cancellation

You can cancel a task group and all of its child tasks by calling the [`cancelAll()`](taskgroup/cancelall().md) method on the task group, or by canceling the task in which the group is running.

If you call `addTask(priority:operation:)` to create a new task in a canceled group, that task is immediately canceled after creation. Alternatively, you can call `asyncUnlessCancelled(priority:operation:)`, which doesn’t create the task if the group has already been canceled. Choosing between these two functions lets you control how to react to cancellation within a group: some child tasks need to run regardless of cancellation, but other tasks are better not even being created when you know they can’t produce useful results.

### Error Handling and Implicit Cancellation

Since it is not possible to explicitly await individual task completions, it is also not possible to “re-throw” an error thrown by one of the child tasks using the same pattern as one would in a [`ThrowingTaskGroup`](throwingtaskgroup.md):

```swift
// ThrowingTaskGroup, pattern not applicable to ThrowingDiscardingTaskGroup
try await withThrowingTaskGroup(of: Void.self) { group in
  group.addTask { try boom() }
  try await group.next() // re-throws "boom"
}
```

Since discarding task groups don’t have access to `next()`, this pattern cannot be used. Instead, a .

The  thrown inside such task group is then retained and thrown out of the `withThrowingDiscardingTaskGroup` method when it returns.

```swift
try await withThrowingDiscardingTaskGroup { group in
  group.addTask { try boom(1) }
  group.addTask { try boom(2, after: .seconds(5)) }
  group.addTask { try boom(3, after: .seconds(5)) }
}
```

Generally, this suits the typical use cases of a discarding task group well, however, if you want to prevent specific errors from canceling the group you can catch them inside the child task’s body like this:

```swift
try await withThrowingDiscardingTaskGroup { group in
  group.addTask {
    do {
      try boom(1)
    } catch is HarmlessError {
      return
    }
  }
  group.addTask {
    try boom(2, after: .seconds(5))
  }
}
```

## See Also

- [struct Task](task.md)
  A unit of asynchronous work.
- [struct TaskGroup](taskgroup.md)
  A group that contains dynamically created child tasks.
- [func withTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout TaskGroup<ChildTaskResult>) async -> GroupResult) async -> GroupResult](withtaskgroup(of:returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [macro Task(name: String?, priority: TaskPriority?)](task(name:priority:).md)
  Wrap the function body in a new top-level task on behalf of the current actor.
- [macro Task(on: any GlobalActor, name: String?, priority: TaskPriority?)](task(on:name:priority:).md)
  Wrap the function body in a new top-level task on behalf of the given actor.
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
- [struct UnsafeCurrentTask](unsafecurrenttask.md)
  An unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withthrowingdiscardingtaskgroup(returning:isolation:body:))*