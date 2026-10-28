# dispatch_block_create_with_qos_class

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new dispatch block from an existing block and the given flags, and assigns it the specified quality-of-service class and relative priority.

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
extern dispatch_block_t dispatch_block_create_with_qos_class(dispatch_block_flags_t flags, dispatch_qos_class_t qos_class, int relative_priority, dispatch_block_t block);
```

## Discussion

The provided block is copied to the heap and retained by the newly created dispatch block.

The returned dispatch block is intended to be submitted to a dispatch queue with [`dispatch_async`](./dispatch_async.md) and related functions, but may also be invoked directly. Both operations can be performed an arbitrary number of times but only the first completed execution of a dispatch block can be waited on with [`dispatch_block_wait`](./dispatch_block_wait.md) or observed with [`dispatch_block_notify`](./dispatch_block_notify.md).

If invoked directly, the returned dispatch block is executed with the assigned QoS class as long as that does not result in a lower QoS class than what is current on the calling thread.

If the returned dispatch block is submitted to a dispatch queue, the QoS class it is executed with depends on the QoS class assigned to the block, the QoS class assigned to the queue and which of the following flags was specified or defaulted to:

- [`DISPATCH_BLOCK_INHERIT_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_inherit_qos_class.md) (default for asynchronous execution)
- [`DISPATCH_BLOCK_ENFORCE_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_enforce_qos_class.md) (default for synchronous execution)

If the returned dispatch block is submitted directly to a serial queue and is configured to execute with a specific QoS class, the system makes a best effort to apply the necessary QoS overrides to ensure that blocks submitted earlier to the serial queue are executed at that same QoS class or higher.

See [`dispatch_block_flags_t`](./dispatch_block_flags_t.md) for more information.

## Parameters

- `flags`: Configuration flags for the block object. For possible values, see [`dispatch_block_flags_t`](./dispatch_block_flags_t.md).

  Passing a value that is not a bitwise OR of valid flags results in `NULL` being returned.
- `qos_class`: The QoS class. For possible values, see [Quality of Service Classes (QoS)](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RelatedDocuments.html#//apple_ref/doc/uid/TP40013929-CH20-SW16).

  Passing `QOS_CLASS_UNSPECIFIED` is equivalent to specifying the [`DISPATCH_BLOCK_NO_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_no_qos_class.md) flag.

  Passing any other value results in `NULL` being returned.
- `relative_priority`: A relative priority within the QoS class.

  This value is a negative offset from the maximum supported scheduler priority for the given class. Passing a value greater than zero or less than `QOS_MIN_RELATIVE_PRIORITY` results in `NULL` being returned.
- `block`: The block to create the dispatch block from.

## See Also

### Creating a Work Item
- [dispatch_block_create](./dispatch_block_create.md)
  Creates a new dispatch block on the heap using an existing block and the given flags.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
- [dispatch_block_flags_t](./dispatch_block_flags_t.md)
  Flags to pass to the [`dispatch_block_create`](./dispatch_block_create.md) and [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_create_with_qos_class)*