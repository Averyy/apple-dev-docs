# dispatch_queue_t

**Framework**: Dispatch  
**Kind**: typealias

A lightweight object to which your application submits blocks for subsequent execution.

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
typealias dispatch_queue_t = DispatchQueue
```

#### Discussion

A dispatch queue invokes blocks submitted to it serially in FIFO order. A serial queue invokes only one block at a time, but independent queues may each invoke their blocks concurrently with respect to each other.

The global concurrent queues invoke blocks in FIFO order but do not wait for their completion, allowing multiple blocks to be invoked concurrently.

The system manages a pool of threads that process dispatch queues and invoke blocks submitted to them. Conceptually, a dispatch queue may have its own thread of execution, and interaction between queues is highly asynchronous.

Dispatch queues are reference counted via calls to [`dispatch_retain`](dispatch_retain.md) and [`dispatch_release`](dispatch_release.md). Pending blocks submitted to a queue also hold a reference to the queue until they have finished. Once all references to a queue have been released, the queue will be deallocated by the system.

## See Also

- [typealias dispatch_group_t](dispatch_group_t.md)
  A group of block objects submitted to a queue for asynchronous invocation.
- [typealias dispatch_io_t](dispatch_io_t.md)
  A dispatch I/O channel.
- [typealias dispatch_object_t](dispatch_object_t.md)
  A dispatch object.
- [typealias dispatch_queue_attr_t](dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [typealias dispatch_queue_serial_executor_t](dispatch_queue_serial_executor_t.md)
- [typealias dispatch_semaphore_t](dispatch_semaphore_t.md)
  A dispatch semaphore object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_t)*