# dispatch_sync_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits an app-defined function for synchronous execution on a dispatch queue.

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
extern void dispatch_sync_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Parameters

- `queue`: The queue on which to submit the function.  This parameter cannot be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter. This parameter cannot be `NULL`.

## See Also

### Executing Tasks Synchronously
- [func sync(execute: () -> Void)](./dispatchqueue/sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func asyncAndWait(execute: () -> Void)](./dispatchqueue/asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.
- [dispatch_async_and_wait_f](./dispatch_async_and_wait_f.md)
  Submits a function-based work item for execution and returns only after it finishes executing.
- [dispatch_barrier_async_and_wait](./dispatch_barrier_async_and_wait.md)
  Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](./dispatch_barrier_async_and_wait_f.md)
  Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_sync_f)*