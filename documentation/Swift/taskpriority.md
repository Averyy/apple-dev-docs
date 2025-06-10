# TaskPriority

**Framework**: Swift  
**Kind**: struct

The priority of a task.

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
struct TaskPriority
```

#### Overview

The executor determines how priority information affects the way tasks are scheduled. The behavior varies depending on the executor currently being used. Typically, executors attempt to run tasks with a higher priority before tasks with a lower priority. However, the semantics of how priority is treated are left up to each platform and `Executor` implementation.

Child tasks automatically inherit their parent task’s priority. Detached tasks created by `detach(priority:operation:)` don’t inherit task priority because they aren’t attached to the current task.

In some situations the priority of a task is elevated — that is, the task is treated as it if had a higher priority, without actually changing the priority of the task:

- If a task runs on behalf of an actor, and a new higher-priority task is enqueued to the actor, then the actor’s current task is temporarily elevated to the priority of the enqueued task. This priority elevation allows the new task to be processed at the priority it was enqueued with.
- If a higher-priority task calls the `get()` method, then the priority of this task increases until the task completes.

In both cases, priority elevation helps you prevent a low-priority task from blocking the execution of a high priority task, which is also known as .

## Topics

### Operators
- [static func != (TaskPriority, TaskPriority) -> Bool](taskpriority/!=(_:_:).md)
### Initializers
- [init?(JobPriority)](taskpriority/init(_:).md)
  Convert this `UnownedJob/Priority` to a [`TaskPriority`](taskpriority.md).
- [init(rawValue: UInt8)](taskpriority/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: UInt8](taskpriority/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [TaskPriority.RawValue](taskpriority/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let background: TaskPriority](taskpriority/background.md)
- [static let `default`: TaskPriority](taskpriority/default.md)
- [static let high: TaskPriority](taskpriority/high.md)
- [static let low: TaskPriority](taskpriority/low.md)
- [static var medium: TaskPriority](taskpriority/medium.md)
- [static var unspecified: TaskPriority](taskpriority/unspecified.md)
- [static let userInitiated: TaskPriority](taskpriority/userinitiated.md)
- [static var userInteractive: TaskPriority](taskpriority/userinteractive.md)
- [static let utility: TaskPriority](taskpriority/utility.md)
### Default Implementations
- [Comparable Implementations](taskpriority/comparable-implementations.md)
- [CustomStringConvertible Implementations](taskpriority/customstringconvertible-implementations.md)
- [Equatable Implementations](taskpriority/equatable-implementations.md)
- [RawRepresentable Implementations](taskpriority/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [RawRepresentable](rawrepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskpriority)*