# dispatch_async

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Submits a block for asynchronous execution on a dispatch queue and returns immediately.

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
extern void dispatch_async(dispatch_queue_t queue, dispatch_block_t block);
```

#### Discussion

This function is the fundamental mechanism for submitting blocks to a dispatch queue. Calls to this function always return immediately after the block is submitted and never wait for the block to be invoked. The target queue determines whether the block is invoked serially or concurrently with respect to other blocks submitted to that same queue. Independent serial queues are processed concurrently with respect to each other.

## Parameters

- `queue`: The queue on which to submit the block. The system retains the queue until the block runs to completion. This parameter cannot be `NULL`.
- `block`: The block to submit to the target dispatch queue. This function performs `Block_copy` and `Block_release` on behalf of callers. This parameter cannot be `NULL`.

## See Also

### Executing Tasks Asynchronously
- [dispatch_async_f](./dispatch_async_f.md)
  Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](./dispatch_after.md)
  Enqueues a block for execution at the specified time.
- [dispatch_after_f](./dispatch_after_f.md)
  Enqueues an app-defined function for execution at the specified time.
- [dispatch_function_t](./dispatch_function_t.md)
  The prototype of functions submitted to dispatch queues.
- [dispatch_block_t](./dispatch_block_t.md)
  The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_async)*