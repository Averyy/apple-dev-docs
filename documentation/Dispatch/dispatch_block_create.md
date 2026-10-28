# dispatch_block_create

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new dispatch block on the heap using an existing block and the given flags.

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
extern dispatch_block_t dispatch_block_create(dispatch_block_flags_t flags, dispatch_block_t block);
```

## Return Value

The newly created dispatch block, or `NULL`.

## Discussion

The provided block is copied to the heap and retained by the newly created dispatch block.

The returned dispatch block is intended to be submitted to a dispatch queue with [`dispatch_async`](./dispatch_async.md) and related functions, but may also be invoked directly. Both operations can be performed an arbitrary number of times but only the first completed execution of a dispatch block can be waited on with [`dispatch_block_wait`](./dispatch_block_wait.md) or observed with [`dispatch_block_notify`](./dispatch_block_notify.md).

If the returned dispatch block is submitted to a dispatch queue, the submitted block instance is associated with the QoS class current at the time of submission, unless one of the following flags assigned a specific QoS class (or no QoS class) at the time of block creation:

- [`DISPATCH_BLOCK_ASSIGN_CURRENT`](./dispatch_block_flags_t/dispatch_block_assign_current.md)
- [`DISPATCH_BLOCK_NO_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_no_qos_class.md)
- [`DISPATCH_BLOCK_DETACHED`](./dispatch_block_flags_t/dispatch_block_detached.md)

The QoS class the block object is executed with also depends on the QoS class assigned to the queue and which of the following flags was specified or defaulted to:

- [`DISPATCH_BLOCK_INHERIT_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_inherit_qos_class.md) (default for asynchronous execution)
- [`DISPATCH_BLOCK_ENFORCE_QOS_CLASS`](./dispatch_block_flags_t/dispatch_block_enforce_qos_class.md) (default for synchronous execution)

If the returned dispatch block is submitted directly to a serial queue and is configured to execute with a specific QoS class, the system makes a best effort to apply the necessary QoS overrides to ensure that blocks submitted earlier to the serial queue are executed at that same QoS class or higher.

See [`dispatch_block_flags_t`](./dispatch_block_flags_t.md) for more information.

## Parameters

- `flags`: Configuration flags for the block object. For possible values, see [`dispatch_block_flags_t`](./dispatch_block_flags_t.md).

  Passing a value that is not a bitwise OR of valid flags results in `NULL` being returned.
- `block`: The block to create the dispatch block from.

## See Also

### Creating a Work Item
- [dispatch_block_create_with_qos_class](./dispatch_block_create_with_qos_class.md)
  Creates a new dispatch block from an existing block and the given flags, and assigns it the specified quality-of-service class and relative priority.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.
- [dispatch_block_flags_t](./dispatch_block_flags_t.md)
  Flags to pass to the [`dispatch_block_create`](./dispatch_block_create.md) and [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_create)*