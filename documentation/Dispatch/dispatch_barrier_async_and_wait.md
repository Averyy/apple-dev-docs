# dispatch_barrier_async_and_wait

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.

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
extern void dispatch_barrier_async_and_wait(dispatch_queue_t queue, dispatch_block_t block);
```

#### Discussion

This function submits work to the specified queue for execution. Unlike [`dispatch_async`](./dispatch_async.md), this function doesn’t return until after the block finishes. Calling this function and targeting the current queue results in deadlock.

When submitted to a concurrent queue, `block` doesn’t run until all previously submitted tasks finish executing, and subsequently submitted tasks don’t execute until after `block` finishes. You use barriers to ensure the correct execution order of relevant work. For example, you might use them in reader/writer schemes where the order of read and write tasks is significant. If you submit the work to a non-concurrent queue, this method behaves identically to [`asyncAndWait(execute:)`](./dispatchqueue/asyncandwait%28execute%29-1udeu.md).

Unlike [`sync(execute:)`](./dispatchqueue/sync%28execute%29-3segw.md), this function respects all attributes of the queue when it executes the block. For example, it respects the quality-of-service level and autorelease frequency of the target queue.

If the runtime has already brought up a thread to service asynchronous work items, the system uses that same thread to execute any synchronous blocks you submitted using this function. If the runtime hasn’t brought up a thread to service asynchronous work items, the system executes these synchronous blocks on the current thread as an optimization. However, these optimizations apply only when `queue` targets a global concurrent queue. If it targets any other queue, the system executes the work on that queue’s thread. For example, if `queue` targets the main queue, the block always runs on the main thread.

Unlike with [`dispatch_async`](./dispatch_async.md), this method doesn’t retain the `queue` object. Because calls to this function are synchronous, it “borrows” the reference of the caller. Moreover, no `Block_copy` is performed on the block.

## Parameters

- `queue`: The queue on which to submit the block. This parameter can’t be `NULL`.
- `block`: The block that contains the work to perform. This block has no return value and no parameters. This parameter can’t be `NULL`.

## See Also

### Creating a Barrier Synchronously
- [dispatch_barrier_sync](./dispatch_barrier_sync.md)
  Submits a barrier block object for execution and waits until that block completes.
- [dispatch_barrier_sync_f](./dispatch_barrier_sync_f.md)
  Submits a barrier function for execution and waits until that function completes.
- [dispatch_barrier_async_and_wait_f](./dispatch_barrier_async_and_wait_f.md)
  Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_barrier_async_and_wait)*