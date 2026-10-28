# dispatch_assert_queue

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Generates an assertion if the current block is not running on the specified dispatch queue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern void dispatch_assert_queue(dispatch_queue_t queue);
```

## Discussion

Use this function inside a block to verify that the block is running on the expected dispatch queue. For example, you might pass the main queue to the `queue` parameter to verify that the block is running on the app’s main thread. If you submitted the current block synchronously, the function recursively checks the context of the submitting block to ensure that it is also running on the expected dispatch queue. If the block is not running on the expected queue, this function asserts, logs an explanation to the system log, and terminates the app.

This function evaluates where the block is actually executing. For example, if you submit the block to a dispatch queue that targets a different queue, the block is considered to be running on the target queue.

Calling this function outside of a block running on a dispatch queue is a programmer error. If you do so, the function asserts and terminates your app.

## Parameters

- `queue`: The dispatch queue where you expect the current block to be running. This parameter must not be `NULL`.

## See Also

### Testing the Execution Context
- [dispatch_assert_queue_barrier](./dispatch_assert_queue_barrier.md)
  Generates an assertion if the current block is not running as a barrier on the specified dispatch queue.
- [dispatch_assert_queue_not](./dispatch_assert_queue_not.md)
  Generates an assertion if the current block is executing on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_assert_queue)*