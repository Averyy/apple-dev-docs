# dispatch_after_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Enqueues an app-defined function for execution at the specified time.

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
extern void dispatch_after_f(dispatch_time_t when, dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

This function waits until the specified time and then asynchronously adds the `work` function to the specified `queue`.

Passing [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) as the `when` parameter is supported, but is not as optimal as calling [`dispatch_async`](./dispatch_async.md) instead. Passing [`DISPATCH_TIME_FOREVER`](./dispatch_time_forever.md) is undefined.

## Parameters

- `when`: The temporal milestone [`dispatch_time`](./dispatch_time.md) or [`dispatch_walltime`](./dispatch_walltime.md) returns.
- `queue`: The queue on which to submit the function. The system retains the queue until the app-defined function runs to completion. This parameter cannot be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined function to invoke on the target queue. The first parameter passed to this function is the value in the  `context` parameter. This parameter cannot be `NULL`.

## See Also

### Executing Tasks Asynchronously
- [dispatch_async](./dispatch_async.md)
  Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_async_f](./dispatch_async_f.md)
  Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](./dispatch_after.md)
  Enqueues a block for execution at the specified time.
- [dispatch_function_t](./dispatch_function_t.md)
  The prototype of functions submitted to dispatch queues.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_after_f)*