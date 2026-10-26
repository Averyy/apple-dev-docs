# DISPATCH_BLOCK_INHERIT_QOS_CLASS

**Framework**: Dispatch  
**Kind**: case  
**Role**: Enumeration Case

Prefer the quality-of-service class associated with the current execution context.

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
DISPATCH_BLOCK_INHERIT_QOS_CLASS
```

#### Discussion

Indicates that execution of a dispatch block submitted to a queue should prefer the QoS class assigned to the queue over the QoS class assigned to the block at the time of submission. The latter will only be used if the queue in question does not have an assigned QoS class, as long as doing so does not result in a QoS class lower than the QoS class inherited from the queue’s target queue. This flag is the default when a dispatch block is submitted to a queue for asynchronous execution and has no effect when the dispatch block is invoked directly. It is ignored if [`DISPATCH_BLOCK_ENFORCE_QOS_CLASS`](./dispatch_block_enforce_qos_class.md) is also passed.

## See Also

### Flags
- [DISPATCH_BLOCK_ASSIGN_CURRENT](./dispatch_block_assign_current.md)
  Set the attributes of the work item to match the attributes of the current execution context.
- [DISPATCH_BLOCK_BARRIER](./dispatch_block_barrier.md)
  Cause the work item to act as a barrier block when submitted to a concurrent queue.
- [DISPATCH_BLOCK_DETACHED](./dispatch_block_detached.md)
  Disassociate the work item’s attributes from the current execution context.
- [DISPATCH_BLOCK_ENFORCE_QOS_CLASS](./dispatch_block_enforce_qos_class.md)
  Prefer the quality-of-service class associated with the block.
- [DISPATCH_BLOCK_NO_QOS_CLASS](./dispatch_block_no_qos_class.md)
  Execute the work item without assigning a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_inherit_qos_class)*