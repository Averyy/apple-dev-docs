# Dispatch Barrier

**Framework**: Dispatch  
**Role**: API Collection

A synchronization point for tasks executing in a concurrent dispatch queue.

## Overview

Use a barrier to synchronize the execution of one or more tasks in your dispatch queue. When you add a barrier to a concurrent dispatch queue, the queue delays the execution of the barrier block (and any tasks submitted after the barrier) until all previously submitted tasks finish executing. After the previous tasks finish executing, the queue executes the barrier block by itself. Once the barrier block finishes, the queue resumes its normal execution behavior.

## Topics

### Creating a Barrier Asynchronously
- [dispatch_barrier_async](./dispatch_barrier_async.md)
  Submits a barrier block for asynchronous execution and returns immediately.
- [dispatch_barrier_async_f](./dispatch_barrier_async_f.md)
  Submits a barrier function for asynchronous execution and returns immediately.
### Creating a Barrier Synchronously
- [dispatch_barrier_sync](./dispatch_barrier_sync.md)
  Submits a barrier block object for execution and waits until that block completes.
- [dispatch_barrier_sync_f](./dispatch_barrier_sync_f.md)
  Submits a barrier function for execution and waits until that function completes.
- [dispatch_barrier_async_and_wait](./dispatch_barrier_async_and_wait.md)
  Submits a work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.
- [dispatch_barrier_async_and_wait_f](./dispatch_barrier_async_and_wait_f.md)
  Submits a function-based work item for synchronous execution and marks the work as a barrier for subsequent concurrent tasks.

## See Also

### Task Synchronization
- [class DispatchSemaphore](./dispatchsemaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Semaphore](./dispatch-semaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-barrier)*