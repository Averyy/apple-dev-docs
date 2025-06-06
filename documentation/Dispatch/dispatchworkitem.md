# DispatchWorkItem

**Framework**: Dispatch  
**Kind**: class

The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class DispatchWorkItem
```

#### Overview

A [`DispatchWorkItem`](dispatchworkitem.md) encapsulates work to be performed on a dispatch queue or within a dispatch group. You can also use a work item as a [`DispatchSource`](dispatchsource.md) event, registration, or cancellation handler.

## Topics

### Creating a Work Item
- [init(qos: DispatchQoS, flags: DispatchWorkItemFlags, block: () -> Void)](dispatchworkitem/init(qos:flags:block:).md)
  Creates a new dispatch work item from an existing block and assigns it the specified quality-of-service class.
- [struct DispatchWorkItemFlags](dispatchworkitemflags.md)
  A set of behaviors for a work item, such as its quality-of-service class and whether to create a barrier or spawn a new detached thread.
### Executing the Work Item
- [func perform()](dispatchworkitem/perform.md)
  Executes the work item’s block synchronously on the current thread.
### Adding a Completion Handler
- [func notify(queue: DispatchQueue, execute: DispatchWorkItem)](dispatchworkitem/notify(queue:execute:).md)
  Schedules the execution of the specified work item after the completion of the current work item.
- [func notify(qos: DispatchQoS, flags: DispatchWorkItemFlags, queue: DispatchQueue, execute: () -> Void)](dispatchworkitem/notify(qos:flags:queue:execute:).md)
  Schedules the execution of the specified work item, with the specified quality-of-service, after the completion of the current work item.
### Waiting for the Completion of a Work Item
- [func wait()](dispatchworkitem/wait.md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchworkitem/wait(timeout:).md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchworkitem/wait(walltimeout:).md)
  Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [struct DispatchTime](dispatchtime.md)
  A point in time relative to the default clock, with nanosecond precision.
- [struct DispatchWallTime](dispatchwalltime.md)
  An absolute point in time according to the wall clock, with microsecond precision.
### Canceling a Work Item
- [func cancel()](dispatchworkitem/cancel.md)
  Cancels the current work item asynchronously.
- [var isCancelled: Bool](dispatchworkitem/iscancelled.md)
  A Boolean value indicating whether the work item has been canceled.
### Initializers
- [init(flags: DispatchWorkItemFlags, block: () -> Void)](dispatchworkitem/init(flags:block:).md)

## See Also

- [class DispatchQueue](dispatchqueue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [class DispatchGroup](dispatchgroup.md)
  A group of tasks that you monitor as a single unit.
- [Dispatch Queue](dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem)*