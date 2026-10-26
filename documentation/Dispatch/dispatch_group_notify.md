# dispatch_group_notify

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules a block object to be submitted to a queue when a group of previously submitted block objects have completed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_group_notify(dispatch_group_t group, dispatch_queue_t queue, dispatch_block_t block);
```

#### Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately.

When the notification block is submitted, the group is empty. The group can either be released with [`dispatch_release`](./dispatch_release.md) or be reused for additional block objects. See [`dispatch_group_async`](./dispatch_group_async.md) for more information.

## Parameters

- `group`: The dispatch group to observe. The group is retained by the system until the block has run to completion. This parameter cannot be `NULL`.
- `queue`: The queue to which the supplied block is submitted when the group completes. The queue is retained by the system until the block has run to completion. This parameter cannot be `NULL`.
- `block`: The block to submit when the group completes. This function performs a `Block_copy` and `Block_release` on behalf of the caller.  This parameter cannot be `NULL`.

## See Also

### Adding a Completion Handler
- [dispatch_group_notify_f](./dispatch_group_notify_f.md)
  Schedules an application-defined function to be submitted to a queue when a group of previously submitted block objects have completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_group_notify)*