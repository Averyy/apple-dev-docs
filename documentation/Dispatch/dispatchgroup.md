# DispatchGroup

**Framework**: Dispatch  
**Kind**: class

A group of tasks that you monitor as a single unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class DispatchGroup
```

#### Overview

Groups allow you to aggregate a set of tasks and synchronize behaviors on the group. You attach multiple work items to a group and schedule them for asynchronous execution on the same queue or different queues. When all work items finish executing, the group executes its completion handler. You can also wait synchronously for all tasks in the group to finish executing.

## Topics

### Creating a Dispatch Group
- [init()](dispatchgroup/init.md)
  Creates a new group to which you can assign block objects.
### Adding a Completion Handler
- [func notify(qos: DispatchQoS, flags: DispatchWorkItemFlags, queue: DispatchQueue, execute: () -> Void)](dispatchgroup/notify(qos:flags:queue:execute:).md)
  Schedules the submission of a block with the specified attributes to a queue when all tasks in the current group have finished executing.
- [func notify(queue: DispatchQueue, work: DispatchWorkItem)](dispatchgroup/notify(queue:work:).md)
  Schedules the submission of a block to a queue when all tasks in the current group have finished executing.
### Waiting for Tasks to Finish Executing
- [func wait()](dispatchgroup/wait.md)
  Waits synchronously for the previously submitted work to finish.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchgroup/wait(timeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchgroup/wait(walltimeout:).md)
  Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
### Updating the Group Manually
- [func enter()](dispatchgroup/enter.md)
  Explicitly indicates that a block has entered the group.
- [func leave()](dispatchgroup/leave.md)
  Explicitly indicates that a block in the group finished executing.

## Relationships

### Inherits From
- [DispatchObject](dispatchobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class DispatchQueue](dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchWorkItem](dispatchworkitem.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Queue](dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup)*