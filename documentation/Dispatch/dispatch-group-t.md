# dispatch_group_t

**Framework**: Dispatch  
**Kind**: typealias

A group of block objects submitted to a queue for asynchronous invocation.

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
typealias dispatch_group_t = DispatchGroup
```

#### Discussion

A dispatch group is a mechanism for monitoring a set of blocks. Your application can monitor the blocks in the group synchronously or asynchronously depending on your needs. By extension, a group can be useful for synchronizing for code that depends on the completion of other tasks.

Note that the blocks in a group may be run on different queues, and each individual block can add more blocks to the group.

The dispatch group keeps track of how many blocks are outstanding, and GCD retains the group until all its associated blocks complete execution.

## See Also

- [typealias dispatch_io_t](dispatch_io_t.md)
  A dispatch I/O channel.
- [typealias dispatch_object_t](dispatch_object_t.md)
  A dispatch object.
- [typealias dispatch_queue_attr_t](dispatch_queue_attr_t.md)
  Attributes describing the behaviors of a dispatch queue.
- [typealias dispatch_queue_serial_executor_t](dispatch_queue_serial_executor_t.md)
- [typealias dispatch_queue_t](dispatch_queue_t.md)
  A lightweight object to which your application submits blocks for subsequent execution.
- [typealias dispatch_semaphore_t](dispatch_semaphore_t.md)
  A dispatch semaphore object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_group_t)*