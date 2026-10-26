# Dispatch Group

**Framework**: Dispatch  
**Role**: API Collection

A group of tasks that you monitor as a single unit.

#### Overview

Groups allow you to aggregate a set of tasks and synchronize behaviors on the group. You attach multiple blocks to a group and schedule them for asynchronous execution on the same queue or different queues. When all blocks finish executing, the group executes its completion handler. You can also wait synchronously for all blocks in the group to finish executing.

## Topics

### Creating a Dispatch Group
- [init()](./dispatchgroup/init%28%29.md)
  Creates a new group to which you can assign block objects.
- [typealias dispatch_group_t](./dispatch_group_t.md)
  A group of block objects submitted to a queue for asynchronous invocation.
- [OS_dispatch_group](./os_dispatch_group.md)
### Updating the Group Manually
- [func enter()](./dispatchgroup/enter%28%29.md)
  Explicitly indicates that a block has entered the group.
- [func leave()](./dispatchgroup/leave%28%29.md)
  Explicitly indicates that a block in the group finished executing.
### Adding Work to the Group
- [dispatch_group_async](./dispatch_group_async.md)
  Schedules a block asynchronously for execution and simultaneously associates it with the specified dispatch group.
- [dispatch_group_async_f](./dispatch_group_async_f.md)
  Submits an application-defined function to a dispatch queue and associates it with the specified dispatch group.
### Adding a Completion Handler
- [dispatch_group_notify](./dispatch_group_notify.md)
  Schedules a block object to be submitted to a queue when a group of previously submitted block objects have completed.
- [dispatch_group_notify_f](./dispatch_group_notify_f.md)
  Schedules an application-defined function to be submitted to a queue when a group of previously submitted block objects have completed.
### Waiting for Tasks to Finish Executing
- [dispatch_group_wait](./dispatch_group_wait.md)
  Waits synchronously for the previously submitted block objects to finish; returns if the blocks do not complete before the specified timeout period has elapsed.

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
- [Dispatch Work Item](./dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Workloop](./workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-group)*