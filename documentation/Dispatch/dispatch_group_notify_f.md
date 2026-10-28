# dispatch_group_notify_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules an application-defined function to be submitted to a queue when a group of previously submitted block objects have completed.

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
extern void dispatch_group_notify_f(dispatch_group_t group, dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately.

When the notification block is submitted, the group is empty, and can be reused for additional blocks. See [`dispatch_group_async`](./dispatch_group_async.md) for more information.

If your app isn’t using ARC, you should call [`dispatch_release`](./dispatch_release.md) on a dispatch group when it’s no longer needed.

## Parameters

- `group`: The dispatch group to observe. The group is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.
- `queue`: The queue to which the supplied block is submitted when the group completes. The queue is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.
- `context`: The application-defined context parameter to pass to the application-defined function.
- `work`: The application-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter.

## See Also

### Adding a Completion Handler
- [dispatch_group_notify](./dispatch_group_notify.md)
  Schedules a block object to be submitted to a queue when a group of previously submitted block objects have completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_group_notify_f)*