# dispatch_barrier_async_f

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a barrier function for asynchronous execution and returns immediately.

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
extern void dispatch_barrier_async_f(dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Discussion

Calls to this function always return immediately after the barrier function is submitted and never wait for that function to be invoked. When the barrier function reaches the front of a private concurrent queue, it is not executed immediately. Instead, the queue waits until its currently executing blocks finish executing. At that point, the queue executes the barrier function by itself. Any blocks submitted after the barrier function are not executed until the barrier function completes.

The queue you specify should be a concurrent queue that you create yourself using the [`dispatch_queue_create`](./dispatch_queue_create.md) function. If the queue you pass to this function is a serial queue or one of the global concurrent queues, this function behaves like the [`dispatch_async`](./dispatch_async.md) function.

## Parameters

- `queue`: The dispatch queue on which to execute the barrier function. The system retains the queue until the function runs to completion. This parameter cannot be `NULL`.
- `context`: The app-defined context parameter to pass to the function.
- `work`: The app-defined barrier function to be executed. The first parameter passed to this function is the value of the `context` parameter. This parameter cannot be `NULL`.

## See Also

### Creating a Barrier Asynchronously
- [dispatch_barrier_async](./dispatch_barrier_async.md)
  Submits a barrier block for asynchronous execution and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_barrier_async_f)*