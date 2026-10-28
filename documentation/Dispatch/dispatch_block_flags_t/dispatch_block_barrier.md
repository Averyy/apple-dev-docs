# DISPATCH_BLOCK_BARRIER

**Framework**: Dispatch  
**Kind**: case  
**Role**: Enumeration Case

Cause the work item to act as a barrier block when submitted to a concurrent queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
DISPATCH_BLOCK_BARRIER
```

## Discussion

Indicates that a dispatch block should act as a barrier block when submitted to a [`DISPATCH_QUEUE_CONCURRENT`](../dispatch_queue_concurrent.md) queue. See [`dispatch_barrier_async`](../dispatch_barrier_async.md) for details. This flag has no effect when the dispatch block is invoked directly.

## See Also

### Flags
- [DISPATCH_BLOCK_ASSIGN_CURRENT](./dispatch_block_assign_current.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [DISPATCH_BLOCK_DETACHED](./dispatch_block_detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [DISPATCH_BLOCK_ENFORCE_QOS_CLASS](./dispatch_block_enforce_qos_class.md)
  Prefer the quality-of-service class associated with the block.
- [DISPATCH_BLOCK_INHERIT_QOS_CLASS](./dispatch_block_inherit_qos_class.md)
  Prefer the quality-of-service class associated with the current execution context.
- [DISPATCH_BLOCK_NO_QOS_CLASS](./dispatch_block_no_qos_class.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_barrier)*