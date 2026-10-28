# DispatchQueue

**Framework**: Dispatch  
**Kind**: class  
**Role**: Class

An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class DispatchQueue
```

## Overview

Dispatch queues are FIFO queues to which your application can submit tasks in the form of block objects. Dispatch queues execute tasks either serially or concurrently. Work submitted to dispatch queues executes on a pool of threads managed by the system. Except for the dispatch queue representing your app’s main thread, the system makes no guarantees about which thread it uses to execute a task.

You schedule work items synchronously or asynchronously. When you schedule a work item synchronously, your code waits until that item finishes execution. When you schedule a work item asynchronously, your code continues executing while the work item runs elsewhere.

> ❗ **Important**:  Attempting to synchronously execute a work item on the main queue results in deadlock.

### Avoiding Excessive Thread Creation

When designing tasks for concurrent execution, do not call methods that block the current thread of execution. When a task scheduled by a concurrent dispatch queue blocks a thread, the system creates additional threads to run other queued concurrent tasks. If too many tasks block, the system may run out of threads for your app.

Another way that apps consume too many threads is by creating too many private concurrent dispatch queues. Because each dispatch queue consumes thread resources, creating additional concurrent dispatch queues exacerbates the thread consumption problem. Instead of creating private concurrent queues, submit tasks to one of the global concurrent dispatch queues. For serial tasks, set the target of your serial queue to one of the global concurrent queues. That way, you can maintain the serialized behavior of the queue while minimizing the number of separate queues creating threads.

## Topics

### Creating a Dispatch Queue
- [class var main: DispatchQueue](./dispatchqueue/main.md)
  The dispatch queue associated with the main thread of the current process.
- [class func global(qos: DispatchQoS.QoSClass) -> DispatchQueue](./dispatchqueue/global%28qos%29.md)
  Returns the global system queue with the specified quality-of-service class.
- [convenience init(label: String, qos: DispatchQoS, attributes: DispatchQueue.Attributes, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency, target: DispatchQueue?)](./dispatchqueue/init%28label,qos,attributes,autoreleasefrequency,target%29.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DispatchQoS.QoSClass](./dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [DispatchQueue.Attributes](./dispatchqueue/attributes.md)
  Attributes that define the behavior of a dispatch queue.
- [DispatchQueue.AutoreleaseFrequency](./dispatchqueue/autoreleasefrequency.md)
  Constants indicating the frequency with which a dispatch queue autoreleases objects.
- [class OS_dispatch_queue_main](./os_dispatch_queue_main-swift.class.md)
  A system-provided dispatch queue that schedules tasks for serial execution on the app’s main thread.
- [class OS_dispatch_queue_global](./os_dispatch_queue_global-swift.class.md)
  A system-provided dispatch queue that schedules tasks for concurrent execution.
- [class DispatchSerialQueue](./dispatchserialqueue.md)
  A custom dispatch queue that schedules tasks for serial execution on an arbitrary thread.
- [class DispatchConcurrentQueue](./dispatchconcurrentqueue.md)
  A custom dispatch queue that schedules tasks for concurrent execution.
- [typealias dispatch_queue_main_t](./dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](./dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](./dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](./dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.
### Executing Tasks Asynchronously
- [func async(execute: DispatchWorkItem)](./dispatchqueue/async%28execute%29.md)
  Schedules a work item for immediate execution, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)](./dispatchqueue/asyncafter%28deadline,execute%29.md)
  Schedules a work item for execution at the specified time, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/asyncafter%28deadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](./dispatchqueue/asyncafter%28walldeadline,execute%29.md)
  Schedules a work item for execution after the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/asyncafter%28walldeadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.
### Executing Tasks Synchronously
- [func sync(execute: DispatchWorkItem)](./dispatchqueue/sync%28execute%29-2fzvo.md)
  Submits a work item for execution on the current queue and returns after that block finishes executing.
- [func sync(execute: () -> Void)](./dispatchqueue/sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func sync<T>(execute: () throws -> T) rethrows -> T](./dispatchqueue/sync%28execute%29-20xby.md)
  Submits a work item for execution and returns the results from that item after it finishes executing.
- [func sync<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](./dispatchqueue/sync%28flags,execute%29.md)
  Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [func asyncAndWait(execute: () -> Void)](./dispatchqueue/asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.
### Executing a Task in Parallel
- [class func concurrentPerform(iterations: Int, execute: (Int) -> Void)](./dispatchqueue/concurrentperform%28iterations,execute%29.md)
  Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.
### Dispatching Work to Groups
- [func async(group: DispatchGroup, execute: DispatchWorkItem)](./dispatchqueue/async%28group,execute%29.md)
  Schedules a work item asynchronously for execution and associates it with the specified dispatch group.
- [func async(group: DispatchGroup?, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/async%28group,qos,flags,execute%29.md)
  Schedules a block asynchronously for execution and optionally associates it with a dispatch group.
### Managing Queue Attributes
- [var label: String](./dispatchqueue/label.md)
  The label you assigned to the dispatch queue at creation time.
- [var qos: DispatchQoS](./dispatchqueue/qos.md)
  The quality-of-service level assgined to the queue.
- [func setTarget(queue: dispatch_queue_t?)](./dispatchobject/settarget%28queue%29.md)
  Specifies the dispatch queue on which to perform work associated with the current object.
### Getting and Setting Contextual Data
- [func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?)](./dispatchqueue/setspecific%28key,value%29.md)
  Sets the key/value data for the specified dispatch queue.
- [func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](./dispatchqueue/getspecific%28key%29-swift.method.md)
  Returns the value for the key associated with this dispatch queue.
- [class func getSpecific<T>(key: DispatchSpecificKey<T>) -> T?](./dispatchqueue/getspecific%28key%29-swift.type.method.md)
  Returns the value for the key associated with the current execution context.
- [class DispatchSpecificKey](./dispatchspecifickey.md)
  A key associated with a specific contextual value on a dispatch queue.
### Managing the Main Dispatch Queue
- [func dispatchMain() -> Never](./dispatchmain%28%29.md)
  Executes blocks submitted to the main queue.
### Scheduling Combine Publishers
- [DispatchQueue.SchedulerTimeType](./dispatchqueue/schedulertimetype.md)
  The scheduler time type used by the dispatch queue.
- [DispatchQueue.SchedulerOptions](./dispatchqueue/scheduleroptions.md)
  A set of options that affect the operation of the dispatch queue scheduler.
### Deprecated
- [class func global(priority: DispatchQueue.GlobalQueuePriority) -> DispatchQueue](./dispatchqueue/global%28priority%29.md)
- [DispatchQueue.GlobalQueuePriority](./dispatchqueue/globalqueuepriority.md)
  Legacy constants for queue priorities.
### Instance Methods
- [func asyncAfterUnsafe(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/asyncafterunsafe%28deadline,qos,flags,execute%29.md)
- [func asyncAfterUnsafe(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/asyncafterunsafe%28walldeadline,qos,flags,execute%29.md)
- [func asyncAndWait<T>(execute: () throws -> T) rethrows -> T](./dispatchqueue/asyncandwait%28execute%29-52p9n.md)
- [func asyncAndWait(execute: DispatchWorkItem)](./dispatchqueue/asyncandwait%28execute%29-pfxy.md)
- [func asyncAndWait<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](./dispatchqueue/asyncandwait%28flags,execute%29.md)
- [func asyncUnsafe(group: DispatchGroup?, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./dispatchqueue/asyncunsafe%28group,qos,flags,execute%29.md)
### Default Implementations
- [Scheduler Implementations](./dispatchqueue/scheduler-implementations.md)

## Relationships

### Inherits From
- [DispatchObject](./dispatchobject.md)
### Inherited By
- [DispatchConcurrentQueue](./dispatchconcurrentqueue.md)
- [OS_dispatch_queue_global](./os_dispatch_queue_global-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Executor](../Swift/executor.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Scheduler](../Combine/scheduler.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TaskExecutor](../Swift/taskexecutor.md)

## See Also

### Queues and Tasks
- [class DispatchWorkItem](./dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [class DispatchGroup](./dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Queue](./dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](./dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](./dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](./workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue)*