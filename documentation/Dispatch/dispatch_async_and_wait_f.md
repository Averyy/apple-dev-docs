# dispatch_async_and_wait_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a function-based work item for execution and returns only after it finishes executing.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern void dispatch_async_and_wait_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

This function submits work to the specified queue for execution. Unlike [`dispatch_async`](./dispatch_async.md), this function doesn’t return until after the block finishes. Calling this function and targeting the current queue results in deadlock.

Unlike [`sync(execute:)`](./dispatchqueue/sync%28execute%29-3segw.md), this function respects all attributes of the queue when it executes the `work` function. For example, it respects the quality-of-service level and autorelease frequency of the target queue.

If the runtime has already brought up a thread to service asynchronous work items, the system uses that same thread to execute the `work` function synchronously. If the runtime hasn’t brought up a thread to service asynchronous work items, the system executes `work` on the current thread as an optimization. However, these optimizations apply only when `queue` targets a global concurrent queue. If it targets any other queue, the system executes the `work` function on that queue’s thread. For example, if `queue` targets the main queue, the function always runs on the main thread.

Unlike with [`dispatch_async`](./dispatch_async.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller.

## Parameters

- `queue`: The queue on which to submit the function. This parameter can’t be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter. This parameter can’t be `NULL`.

## See Also

### Executing Tasks Synchronously
- [func sync(execute: () -> Void)](./dispatchqueue/sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [dispatch_sync_f](./dispatch_sync_f.md)
  Submits an app-defined function for synchronous execution on a dispatch queue.
- [func asyncAndWait(execute: () -> Void)](./dispatchqueue/asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.
- [dispatch_barrier_async_and_wait](./dispatch_barrier_async_and_wait.md)
  Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](./dispatch_barrier_async_and_wait_f.md)
  Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_async_and_wait_f)*