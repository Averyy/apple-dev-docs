# DISPATCH_BLOCK_NO_QOS_CLASS

**Framework**: Dispatch  
**Kind**: case  
**Role**: Enumeration Case

Execute the work item without assigning a quality-of-service class.

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
DISPATCH_BLOCK_NO_QOS_CLASS
```

## Discussion

Indicates that a dispatch block should be not be assigned a QoS class. If invoked directly, the block object will be executed with the QoS class of the calling thread. If the block object is submitted to a queue, this replaces the default behavior of associating the submitted block instance with the QoS class current at the time of submission. This flag is ignored if a specific QoS class is assigned with the [`dispatch_block_create_with_qos_class`](../dispatch_block_create_with_qos_class.md) function.

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
- [DISPATCH_BLOCK_INHERIT_QOS_CLASS](./dispatch_block_inherit_qos_class.md)
  Prefer the quality-of-service class associated with the current execution context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_no_qos_class)*