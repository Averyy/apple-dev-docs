# dispatch_barrier_async_and_wait_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.

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
extern void dispatch_barrier_async_and_wait_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

This function submits work to the specified queue for execution. Unlike [`dispatch_async`](./dispatch_async.md), this function does not return until after the `work` function finishes. Calling this function and targeting the current queue results in deadlock.

When submitted to a concurrent queue, the `work` function doesn’t run until all previously submitted tasks finish executing, and subsequently submitted tasks don’t execute until after the `work` function finishes. You use barriers to ensure the correct execution order of relevant work. For example, you might use them in reader/writer schemes where the order of read and write tasks is significant. If you submit the work to a nonconcurrent queue, this method behaves identically to [`asyncAndWait(execute:)`](./dispatchqueue/asyncandwait%28execute%29-1udeu.md).

Unlike [`sync(execute:)`](./dispatchqueue/sync%28execute%29-3segw.md), this function respects all attributes of the queue when it executes the `work` function. For example, it respects the quality-of-service level and autorelease frequency of the target queue.

If the runtime has already brought up a thread to service asynchronous work items, the system uses that same thread to execute any synchronous tasks you submitted using this function. If the runtime hasn’t brought up a thread to service asynchronous work items, the sytem executes these synchronous tasks on the current thread as an optimization. However, these optimizations apply only when `queue` targets a global concurrent queue. If it targets any other queue, the system executes the work on that queue’s thread. For example, if `queue` targets the main queue, the `work` function always runs on the main thread.

Unlike with [`dispatch_async`](./dispatch_async.md), this method doesn’t retain the `queue` object. Because calls to this function are synchronous, it “borrows” the reference of the caller.

## Parameters

- `queue`: The queue on which to submit the function. This parameter cannot be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter. This parameter cannot be `NULL`.

## See Also

### Creating a Barrier Synchronously
- [dispatch_barrier_sync](./dispatch_barrier_sync.md)
  Submits a barrier block object for execution and waits until that block completes.
- [dispatch_barrier_sync_f](./dispatch_barrier_sync_f.md)
  Submits a barrier function for execution and waits until that function completes.
- [dispatch_barrier_async_and_wait](./dispatch_barrier_async_and_wait.md)
  Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_barrier_async_and_wait_f)*