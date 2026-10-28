# dispatch_block_wait

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Waits synchronously until execution of the specified dispatch block has completed or until the specified timeout has elapsed.

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
extern intptr_t dispatch_block_wait(dispatch_block_t block, dispatch_time_t timeout);
```

## Return Value

Returns zero if the dispatch block completed within the specified timeout, or non-zero if the block timed out.

## Discussion

This function returns immediately if execution of the block object has already completed.

It is not possible to wait for multiple executions of the same block object with this interface. Instead, use [`dispatch_group_wait`](./dispatch_group_wait.md) for that purpose.

A single dispatch block may either be waited on once and executed once, or it may be executed any number of times. The behavior of any other combination is undefined. Submission to a dispatch queue counts as an execution, even if cancellation using the [`dispatch_block_cancel`](./dispatch_block_cancel.md) function means the block’s code never runs.

The result of calling this function from multiple threads simultaneously with the same dispatch block is undefined, but note that doing so would violate the rules described in the previous paragraph.

If this function returns indicating that the specified timeout has elapsed, then that invocation does not count as the one allowed wait.

If at the time this function is called, the specified dispatch block has been submitted directly to a serial queue, the system makes a best effort to apply the necessary QoS overrides to ensure that the block and any blocks submitted earlier to that serial queue are executed at the QoS class (or higher) of the thread calling [`dispatch_block_wait`](./dispatch_block_wait.md).

## Parameters

- `block`: The dispatch block to wait on.

  The result of passing `NULL` or a block object not returned by the [`dispatch_block_create`](./dispatch_block_create.md) or [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) function is undefined.
- `timeout`: When to timeout. For more information, see [`dispatch_time_t`](./dispatch_time_t.md).

  As a convenience, the [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) and [`DISPATCH_TIME_FOREVER`](./dispatch_time_forever.md) constants are provided to have this function immediately return or wait indefinitely, respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_wait)*