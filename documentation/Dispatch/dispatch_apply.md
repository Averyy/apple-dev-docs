# dispatch_apply

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a single block to the dispatch queue and causes the block to be executed the specified number of times.

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
extern void dispatch_apply(size_t iterations, dispatch_queue_t queue, void (^block)(size_t iteration));
```

## Discussion

This function submits a block to a dispatch queue for multiple invocations and waits for all iterations of the task block to complete before returning. If the target queue is a concurrent queue returned by [`dispatch_get_global_queue`](./dispatch_get_global_queue.md), the block can be invoked concurrently, and it must therefore be reentrant-safe. Using this function with a concurrent queue can be useful as an efficient parallel `for` loop.

The current index of iteration is passed to each invocation of the block.

## Parameters

- `iterations`: The number of times to execute the block.
- `queue`: The queue on which to submit the block. It is recommended that you specify [`DISPATCH_APPLY_AUTO`](./dispatch_apply_auto.md) for this parameter, as that causes the block to run on a queue whose quality-of-service class is most appropriate for the current execution context.
- `block`: The application-defined function to be submitted. This parameter cannot be `NULL`. This block has no return value and takes one parameter:

  - **iteration**: The current iteration index.

## See Also

### Executing a Task in Parallel
- [dispatch_apply_f](./dispatch_apply_f.md)
  Submits a single function to the dispatch queue and causes the function to be executed the specified number of times.
- [DISPATCH_APPLY_AUTO](./dispatch_apply_auto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_apply)*