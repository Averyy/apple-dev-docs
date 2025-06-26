# ThrowingTaskGroup

**Framework**: Swift  
**Kind**: struct

A group that contains throwing, dynamically created child tasks.

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
@frozen
struct ThrowingTaskGroup<ChildTaskResult, Failure> where ChildTaskResult : Sendable, Failure : Error
```

#### Overview

To create a throwing task group, call the `withThrowingTaskGroup(of:returning:body:)` method.

Don’t use a task group from outside the task where you created it. In most cases, the Swift type system prevents a task group from escaping like that because adding a child task to a task group is a mutating operation, and mutation operations can’t be performed from concurrent execution contexts like a child task.

##### Task Execution Order

Tasks added to a task group execute concurrently, and may be scheduled in any order.

##### Cancellation Behavior

A task group becomes cancelled in one of the following ways:

- when [`cancelAll()`](throwingtaskgroup/cancelall().md) is invoked on it,
- when an error is thrown out of the `withThrowingTaskGroup(...) { }` closure,
- when the [`Task`](task.md) running this task group is cancelled.

Since a `ThrowingTaskGroup` is a structured concurrency primitive, cancellation is automatically propagated through all of its child-tasks (and their child tasks).

A cancelled task group can still keep adding tasks, however they will start being immediately cancelled, and may act accordingly to this. To avoid adding new tasks to an already cancelled task group, use `addTaskUnlessCancelled(priority:body:)` rather than the plain `addTask(priority:body:)` which adds tasks unconditionally.

For information about the language-level concurrency model that `ThrowingTaskGroup` is part of, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

## Topics

### Adding Tasks to a Throwing Task Group
- [func addTask(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
### Accessing Individual Results
- [func next() async throws -> ChildTaskResult?](throwingtaskgroup/next.md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult(isolation:).md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [var isEmpty: Bool](throwingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
- [func waitForAll(isolation: isolated (any Actor)?) async throws](throwingtaskgroup/waitforall(isolation:).md)
  Wait for all of the group’s remaining tasks to complete.
### Accessing an Asynchronous Sequence of Results
- [func makeAsyncIterator() -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator](throwingtaskgroup/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](throwingtaskgroup/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](throwingtaskgroup/compactmap(_:)-944nh.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](throwingtaskgroup/compactmap(_:)-7mgi5.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](throwingtaskgroup/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](throwingtaskgroup/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](throwingtaskgroup/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](throwingtaskgroup/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](throwingtaskgroup/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](throwingtaskgroup/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](throwingtaskgroup/map(_:)-58nrv.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](throwingtaskgroup/map(_:)-4a4ju.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](throwingtaskgroup/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](throwingtaskgroup/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](throwingtaskgroup/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](throwingtaskgroup/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> AsyncPrefixSequence<Self>](throwingtaskgroup/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](throwingtaskgroup/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](throwingtaskgroup/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](throwingtaskgroup/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Canceling Tasks
- [var isCancelled: Bool](throwingtaskgroup/iscancelled.md)
  A Boolean value that indicates whether the group was canceled.
- [func cancelAll()](throwingtaskgroup/cancelall.md)
  Cancel all of the remaining tasks in the group.
### Supporting Types
- [ThrowingTaskGroup.Element](throwingtaskgroup/element.md)
  The type of element produced by this asynchronous sequence.
- [ThrowingTaskGroup.Iterator](throwingtaskgroup/iterator.md)
  A type that provides an iteration interface over the results of tasks added to the group.
- [ThrowingTaskGroup.AsyncIterator](throwingtaskgroup/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Deprecated
- [func add(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) async -> Bool](throwingtaskgroup/add(priority:operation:).md)
- [func async(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/async(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/asyncunlesscancelled(priority:operation:).md)
- [func spawn(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/spawn(priority:operation:).md)
- [func spawnUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/spawnunlesscancelled(priority:operation:).md)
### Instance Methods
- [func addImmediateTask(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addimmediatetask(name:priority:operation:).md)
  Create and immediately start running a new child task in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addimmediatetaskunlesscancelled(name:priority:operation:).md)
  Create and immediately start running a new child task in the context of the calling thread/task.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(name:executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func next(isolation: isolated (any Actor)?) async throws -> ChildTaskResult?](throwingtaskgroup/next(isolation:).md)
  Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
### Default Implementations
- [AsyncSequence Implementations](throwingtaskgroup/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](asyncsequence.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup)*