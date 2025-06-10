# Concurrency

**Framework**: Swift

Perform asynchronous and parallel operations.

## Topics

### Essentials
- [Code-along: Elevating an app with Swift concurrency](code-along-elevating-an-app-with-swift-concurrency.md)
  Code along with the WWDC presenter to elevate a SwiftUI app with Swift concurrency.
- [Updating an app to use strict concurrency](updating-an-app-to-use-strict-concurrency.md)
  Use this code to follow along with a guide to migrating your code to take advantage of the full concurrency protection that the Swift 6 language mode provides.
- [Updating an App to Use Swift Concurrency](updating_an_app_to_use_swift_concurrency.md)
  Improve your app’s performance by refactoring your code to take advantage of asynchronous functions in Swift.
### Tasks
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
- [func withThrowingDiscardingTaskGroup<GroupResult>(returning: GroupResult.Type, isolation: isolated (any Actor)?, body: (inout ThrowingDiscardingTaskGroup<any Error>) async throws -> GroupResult) async throws -> GroupResult](withthrowingdiscardingtaskgroup(returning:isolation:body:).md)
  Starts a new scope that can contain a dynamic number of child tasks.
- [struct UnsafeCurrentTask](unsafecurrenttask.md)
  An unsafe reference to the current task.
### Asynchronous Sequences
- [protocol AsyncSequence](asyncsequence.md)
  A type that provides asynchronous, sequential, iterated access to its elements.
- [struct AsyncStream](asyncstream.md)
  An asynchronous sequence generated from a closure that calls a continuation to produce new elements.
- [struct AsyncThrowingStream](asyncthrowingstream.md)
  An asynchronous sequence generated from an error-throwing closure that calls a continuation to produce new elements.
### Continuations
- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.
### Actors
- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [actor MainActor](mainactor.md)
  A singleton actor whose executor is equivalent to the main dispatch queue.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [protocol SendableMetatype](sendablemetatype.md)
  A type `T` whose metatype `T.Type` is `Sendable`.
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)
### Task-Local Storage
- [class TaskLocal](tasklocal.md)
  Wrapper type that defines a task-local value key.
- [macro TaskLocal()](tasklocal().md)
  Macro that introduces a [`TaskLocal`](tasklocal.md) binding.
### Executors
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
- [func withTaskExecutorPreference<T, Failure>((any TaskExecutor)?, isolation: isolated (any Actor)?, operation: () async throws(Failure) -> T) async throws(Failure) -> T](withtaskexecutorpreference(_:isolation:operation:).md)
  Configure the current task hierarchy’s task executor preference to the passed [`TaskExecutor`](taskexecutor.md), and execute the passed in closure by immediately hopping to that executor.
### Main and Task Executors
- [protocol MainExecutor](mainexecutor.md)
  The main executor must conform to these three protocols; we have to make this a protocol for compatibility with Embedded Swift.
- [protocol RunLoopExecutor](runloopexecutor.md)
  An executor that is backed by some kind of run loop.
- [protocol SchedulableExecutor](schedulableexecutor.md)
- [protocol ExecutorFactory](executorfactory.md)
  An ExecutorFactory is used to create the default main and task executors.
- [struct PlatformExecutorFactory](platformexecutorfactory.md)
- [class CFMainExecutor](cfmainexecutor.md)
- [class CFTaskExecutor](cftaskexecutor.md)
- [class DispatchGlobalTaskExecutor](dispatchglobaltaskexecutor.md)
- [class DispatchMainExecutor](dispatchmainexecutor.md)
- [class DummyMainExecutor](dummymainexecutor.md)
- [class DummyTaskExecutor](dummytaskexecutor.md)
### Deprecated
- [struct Job](job.md)
  Deprecated equivalent of [`ExecutorJob`](executorjob.md).

## See Also

- [Input and Output](input-and-output.md)
  Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md)
  Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md)
  Generate boilerplate code and perform other compile-time operations.
- [Key-Path Expressions](key-path-expressions.md)
  Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md)
  Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md)
  Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md)
  Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md)
  Work with prefix, postfix, and infix operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/concurrency)*