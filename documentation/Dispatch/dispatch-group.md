# Dispatch Group

**Framework**: Dispatch

A group of tasks that you monitor as a single unit.

#### Overview

Groups allow you to aggregate a set of tasks and synchronize behaviors on the group. You attach multiple blocks to a group and schedule them for asynchronous execution on the same queue or different queues. When all blocks finish executing, the group executes its completion handler. You can also wait synchronously for all blocks in the group to finish executing.

## Topics

### Creating a Dispatch Group
- [init()](dispatchgroup/init.md)
  Creates a new group to which you can assign block objects.
- [typealias dispatch_group_t](dispatch_group_t.md)
  A group of block objects submitted to a queue for asynchronous invocation.
### Updating the Group Manually
- [func enter()](dispatchgroup/enter.md)
  Explicitly indicates that a block has entered the group.
- [func leave()](dispatchgroup/leave.md)
  Explicitly indicates that a block in the group finished executing.

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
- [Workloop](workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-group)*