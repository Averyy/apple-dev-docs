# Workloop

**Framework**: Dispatch

A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.

#### Overview

A workloop is a priority-ordered dispatch queue that uses QoS levels to determine the execution order of tasks. Before it starts executing each new task, the queue evaluates the QoS levels of currently enqueued tasks and selects the one with the highest priority. Tasks with the QoS level `QOS_CLASS_USER_INTERACTIVE` have the highest priority, followed by tasks with the `QOS_CLASS_USER_INITIATED` priority, and so on.

A workloop is a type of [`dispatch_queue_t`](dispatch_queue_t.md) object, and you use the same functions to enqueue new tasks. For example, use the [`dispatch_async`](dispatch_async.md) function to enqueue a task asynchronously.

## Topics

### Creating a Dispatch Workloop
- [typealias dispatch_workloop_t](dispatch_workloop_t.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
### Executing Tasks Synchronously
- [func sync(execute: () -> Void)](dispatchqueue/sync(execute:)-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func asyncAndWait(execute: () -> Void)](dispatchqueue/asyncandwait(execute:)-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.
### Managing Queue Attributes
- [func setTarget(queue: dispatch_queue_t?)](dispatchobject/settarget(queue:).md)
  Specifies the dispatch queue on which to perform work associated with the current object.

## See Also

- [class DispatchQueue](dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchWorkItem](dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [class DispatchGroup](dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Queue](dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md)
  A group of tasks that you monitor as a single unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/workloop)*