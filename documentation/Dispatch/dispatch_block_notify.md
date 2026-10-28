# dispatch_block_notify

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules a notification block to be submitted to a queue when the execution of a specified dispatch block has completed.

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
extern void dispatch_block_notify(dispatch_block_t block, dispatch_queue_t queue, dispatch_block_t notification_block);
```

## Discussion

This function submits the notification block immediately if execution of the observed block object has already completed.

It is not possible to be notified of multiple executions of the same block object with this interface. Instead, use the [`dispatch_group_notify`](./dispatch_group_notify.md) function for that purpose.

A single dispatch block may either be observed one or more times and executed once, or it may be executed any number of times. The behavior of any other combination is undefined. Submission to a dispatch queue counts as an execution, even if cancellation using the [`dispatch_block_cancel`](./dispatch_block_cancel.md) function means the block’s code never runs.

If multiple notification blocks are scheduled for a single block object, there is no defined order in which the notification blocks are submitted to their associated queues.

## Parameters

- `block`: The dispatch block to observe.

  The result of passing `NULL` or a block object not returned by the [`dispatch_block_create`](./dispatch_block_create.md) or [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) function is undefined.
- `queue`: The queue to which the supplied notification block is submitted when the observed block completes.
- `notification_block`: The notification block to submit when the observed block object completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_notify)*