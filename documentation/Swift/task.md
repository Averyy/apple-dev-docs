# Task

**Framework**: Swift  
**Kind**: struct

A unit of asynchronous work.

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
struct Task<Success, Failure> where Success : Sendable, Failure : Error
```

#### Overview

When you create an instance of `Task`, you provide a closure that contains the work for that task to perform. Tasks can start running immediately after creation; you don’t explicitly start or schedule them. After creating a task, you use the instance to interact with it — for example, to wait for it to complete or to cancel it. It’s not a programming error to discard a reference to a task without waiting for that task to finish or canceling it. A task runs regardless of whether you keep a reference to it. However, if you discard the reference to a task, you give up the ability to wait for that task’s result or cancel the task.

To support operations on the current task, which can be either a detached task or child task, `Task` also exposes class methods like `yield()`. Because these methods are asynchronous, they’re always invoked as part of an existing task.

Only code that’s running as part of the task can interact with that task. To interact with the current task, you call one of the static methods on `Task`.

A task’s execution can be seen as a series of periods where the task ran. Each such period ends at a suspension point or the completion of the task. These periods of execution are represented by instances of `PartialAsyncTask`. Unless you’re implementing a custom executor, you don’t directly interact with partial tasks.

For information about the language-level concurrency model that `Task` is part of, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/).

### Task Cancellation

Tasks include a shared mechanism for indicating cancellation, but not a shared implementation for how to handle cancellation. Depending on the work you’re doing in the task, the correct way to stop that work varies. Likewise, it’s the responsibility of the code running as part of the task to check for cancellation whenever stopping is appropriate. In a long-task that includes multiple pieces, you might need to check for cancellation at several points, and handle cancellation differently at each point. If you only need to throw an error to stop the work, call the `Task.checkCancellation()` function to check for cancellation. Other responses to cancellation include returning the work completed so far, returning an empty result, or returning `nil`.

Cancellation is a purely Boolean state; there’s no way to include additional information like the reason for cancellation. This reflects the fact that a task can be canceled for many reasons, and additional reasons can accrue during the cancellation process.

##### Task Closure Lifetime

Tasks are initialized by passing a closure containing the code that will be executed by a given task.

After this code has run to completion, the task has completed, resulting in either a failure or result value, this closure is eagerly released.

Retaining a task object doesn’t indefinitely retain the closure, because any references that a task holds are released after the task completes. Consequently, tasks rarely need to capture weak references to values.

For example, in the following snippet of code it is not necessary to capture the actor as `weak`, because as the task completes it’ll let go of the actor reference, breaking the reference cycle between the Task and the actor holding it.

```swift
struct Work: Sendable {}

actor Worker {
    var work: Task<Void, Never>?
    var result: Work?

    deinit {
        // even though the task is still retained,
        // once it completes it no longer causes a reference cycle with the actor

        print("deinit actor")
    }

    func start() {
        work = Task {
            print("start task work")
            try? await Task.sleep(for: .seconds(3))
            self.result = Work() // we captured self
            print("completed task work")
            // but as the task completes, this reference is released
        }
        // we keep a strong reference to the task
    }
}
```

And using it like this:

```swift
await Worker().start()
```

Note that the actor is only retained by the start() method’s use of `self`, and that the start method immediately returns, without waiting for the unstructured `Task` to finish. Once the task is completed and its closure is destroyed, the strong reference to the actor is also released allowing the actor to deinitialize as expected.

Therefore, the above call will consistently result in the following output:

```other
start task work
completed task work
deinit actor
```

## Topics

### Creating a Task
- [init(priority: TaskPriority?, operation: sending () async -> Success)](task/init(priority:operation:)-7f0zv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(priority:operation:)-ntwf.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(executorpreference:priority:operation:)-7zpzv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(executorpreference:priority:operation:)-6o27o.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [static func detached(priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Failure>](task/detached(priority:operation:)-d24l.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task.
- [static func detached(priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, Failure>](task/detached(priority:operation:)-1g00u.md)
  Runs the given throwing operation asynchronously as part of a new top-level task.
- [static func detached(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Failure>](task/detached(executorpreference:priority:operation:)-1y7ms.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task.
- [static func detached(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, Failure>](task/detached(executorpreference:priority:operation:)-7vnfx.md)
  Runs the given throwing operation asynchronously as part of a new top-level task.
- [static var currentPriority: TaskPriority](task/currentpriority.md)
  The current task’s priority.
- [static var basePriority: TaskPriority?](task/basepriority.md)
  The current task’s base priority.
- [func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)?) async throws(E) -> T](withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:).md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.
### Accessing Results
- [var value: Success](task/value-60t02.md)
  The result from a throwing task, after it completes.
- [var value: Success](task/value-40dtq.md)
  The result from a nonthrowing task, after it completes.
- [var result: Result<Success, Failure>](task/result.md)
  The result or error from a throwing task, after it completes.
### Canceling Tasks
- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](task/cancel.md)
  Cancels this task.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static var isCancelled: Bool](task/iscancelled-swift.type.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](task/checkcancellation.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](withtaskcancellationhandler(handler:operation:).md)
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](withtaskcancellationhandler(operation:oncancel:isolation:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
### Suspending Execution
- [static func yield() async](task/yield.md)
  Suspends the current task and allows other tasks to execute.
- [static func sleep(nanoseconds: UInt64) async throws](task/sleep(nanoseconds:).md)
  Suspends the current task for at least the given duration in nanoseconds.
- [static func sleep<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(for:tolerance:clock:).md)
  Suspends the current task for the given duration.
- [static func sleep<C>(until: C.Instant, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(until:tolerance:clock:).md)
  Suspends the current task until the given deadline within a tolerance.
### Comparing Tasks
- [static func == (Task<Success, Failure>, Task<Success, Failure>) -> Bool](task/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](task/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](task/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](task/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Deprecated
- [typealias Group](task/group.md)
- [typealias Handle](task/handle.md)
- [typealias Priority](task/priority.md)
- [static func CancellationError() -> CancellationError](task/cancellationerror.md)
- [func getResult() async -> Result<Success, Failure>](task/getresult.md)
- [func get() async throws -> Success](task/get-4i2gt.md)
- [static func sleep(UInt64) async](task/sleep(_:).md)
- [static func suspend() async](task/suspend.md)
- [static func runDetached(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, Failure>](task/rundetached(priority:operation:).md)
- [static func withCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](task/withcancellationhandler(handler:operation:).md)
### Initializers
- [init(name: String?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:priority:operation:)-2dll5.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:priority:operation:)-43wmk.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
### Instance Methods
- [func escalatePriority(to: TaskPriority)](task/escalatepriority(to:).md)
  Manually escalate the task `priority` of this task to the `newPriority`.
- [func get() async -> Success](task/get-4ohks.md)
### Type Properties
- [static var currentExecutor: any Executor](task/currentexecutor.md)
  Get the current executor; this is the executor that the currently executing task is executing on.
- [static var currentSchedulableExecutor: (any SchedulableExecutor)?](task/currentschedulableexecutor.md)
  Get the current  executor, if any.
- [static var defaultExecutor: any TaskExecutor](task/defaultexecutor.md)
  The default or global executor, which is the default place in which we run tasks.
- [static var name: String?](task/name.md)
  Returns the human-readable name of the current task, if it was set during the tasks’ creation.
- [static var preferredExecutor: (any TaskExecutor)?](task/preferredexecutor.md)
  Get the preferred executor for the current `Task`, if any.
### Type Methods
- [static func detached(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, Failure>](task/detached(name:priority:operation:)-795w1.md)
  Runs the given throwing operation asynchronously as part of a new top-level task.
- [static func detached(name: String?, priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Failure>](task/detached(name:priority:operation:)-9xki7.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task.
- [static func startSynchronously(name: String?, priority: TaskPriority?, sending () async throws -> Success) -> Task<Success, Never>](task/startsynchronously(name:priority:_:)-3kl43.md)
  Create and immediately start running a new task in the context of the calling thread/task.
- [static func startSynchronously(name: String?, priority: TaskPriority?, sending () async throws -> Success) -> Task<Success, any Error>](task/startsynchronously(name:priority:_:)-6szf8.md)
  Create and immediately start running a new task in the context of the calling thread/task.
- [static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning: BodyResult.Type, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult](task/withgroup(resulttype:returning:body:).md)
### Default Implementations
- [Equatable Implementations](task/equatable-implementations.md)
- [Hashable Implementations](task/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

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
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](withthrowingdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct UnsafeCurrentTask](unsafecurrenttask.md)
  An unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task)*