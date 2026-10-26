# Dispatch Work Item

**Framework**: Dispatch  
**Role**: API Collection

The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.

#### Overview

A dispatch work item encapsulates work to be performed on a dispatch queue or within a dispatch group. You can also use a work item as a dispatch source event, registration, or cancellation handler.

## Topics

### Creating a Work Item
- [dispatch_block_create](./dispatch_block_create.md)
  Creates a new dispatch block on the heap using an existing block and the given flags.
- [dispatch_block_create_with_qos_class](./dispatch_block_create_with_qos_class.md)
  Creates a new dispatch block from an existing block and the given flags, and assigns it the specified quality-of-service class and relative priority.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
- [dispatch_block_flags_t](./dispatch_block_flags_t.md)
  Flags to pass to the [`dispatch_block_create`](./dispatch_block_create.md) and [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) functions.
### Scheduling Work Items
- [dispatch_block_perform](./dispatch_block_perform.md)
  Creates, synchronously executes, and releases a dispatch block from the specified block and flags.
### Adding a Completion Handler
- [dispatch_block_notify](./dispatch_block_notify.md)
  Schedules a notification block to be submitted to a queue when the execution of a specified dispatch block has completed.
### Delaying Execution of a Work Item
- [dispatch_block_wait](./dispatch_block_wait.md)
  Waits synchronously until execution of the specified dispatch block has completed or until the specified timeout has elapsed.
### Canceling a Work Item
- [dispatch_block_cancel](./dispatch_block_cancel.md)
  Cancels the specified dispatch block asynchronously.
- [dispatch_block_testcancel](./dispatch_block_testcancel.md)
  Tests whether the given dispatch block has been canceled.

## See Also

### Queues and Tasks
- [class DispatchQueue](./dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchWorkItem](./dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [class DispatchGroup](./dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Queue](./dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Group](./dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](./workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-work-item)*