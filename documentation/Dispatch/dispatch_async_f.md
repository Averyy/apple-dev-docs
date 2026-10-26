# dispatch_async_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.

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
extern void dispatch_async_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

#### Discussion

This function is the fundamental mechanism for submitting app-defined functions to a dispatch queue. Calls to this function always return immediately after the function is submitted and never wait for it to be invoked. The target queue determines whether the function is invoked serially or concurrently with respect to other tasks submitted to that same queue. Serial queues are processed concurrently with respect to each other.

## Parameters

- `queue`: The queue on which to submit the function. The system retains the queue until the function runs to completion. This parameter cannot be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined function to invoke on the target queue. The first parameter passed to this function is the value of the `context` parameter. This parameter cannot be `NULL`.

## See Also

### Executing Tasks Asynchronously
- [dispatch_async](./dispatch_async.md)
  Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](./dispatch_after.md)
  Enqueues a block for execution at the specified time.
- [dispatch_after_f](./dispatch_after_f.md)
  Enqueues an app-defined function for execution at the specified time.
- [dispatch_function_t](./dispatch_function_t.md)
  The prototype of functions submitted to dispatch queues.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_async_f)*