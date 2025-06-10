# Task(name:priority:)

**Framework**: Swift  
**Kind**: macro

Wrap the function body in a new top-level task on behalf of the current actor.

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
@attached
(body) macro Task(name: String? = nil, priority: TaskPriority? = nil)
```

## See Also

- [struct Task](task.md)
  A unit of asynchronous work.
- [struct TaskGroup](taskgroup.md)
  A group that contains dynamically created child tasks.
- [func withTaskGroup<ChildTaskResult, GroupResult>(of: ChildTaskResult.Type, returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout TaskGroup<ChildTaskResult>) async -> GroupResult) async -> GroupResult](withtaskgroup(of:returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
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
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](withthrowingdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct UnsafeCurrentTask](unsafecurrenttask.md)
  An unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task(name:priority:))*