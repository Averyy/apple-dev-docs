# dispatch_barrier_async

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a barrier block for asynchronous execution and returns immediately.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_barrier_async(dispatch_queue_t queue, dispatch_block_t block);
```

#### Discussion

Calls to this function always return immediately after the block is submitted and never wait for the block to be invoked. When the barrier block reaches the front of a private concurrent queue, it is not executed immediately. Instead, the queue waits until its currently executing blocks finish executing. At that point, the barrier block executes by itself. Any blocks submitted after the barrier block are not executed until the barrier block completes.

The queue you specify should be a concurrent queue that you create yourself using the [`dispatch_queue_create`](./dispatch_queue_create.md) function. If the queue you pass to this function is a serial queue or one of the global concurrent queues, this function behaves like the [`dispatch_async`](./dispatch_async.md) function.

## Parameters

- `queue`: The dispatch queue on which to execute the barrier block. The system retains the queue until the block runs to completion. This parameter cannot be `NULL`.
- `block`: The barrier block to submit to the target dispatch queue. This block is copied and retained until it finishes executing, at which point it is released. This parameter cannot be `NULL`.

## See Also

### Creating a Barrier Asynchronously
- [dispatch_barrier_async_f](./dispatch_barrier_async_f.md)
  Submits a barrier function for asynchronous execution and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_barrier_async)*