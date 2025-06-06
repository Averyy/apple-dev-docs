# Dispatch Barrier

**Framework**: Dispatch

A synchronization point for tasks executing in a concurrent dispatch queue.

#### Overview

Use a barrier to synchronize the execution of one or more tasks in your dispatch queue. When you add a barrier to a concurrent dispatch queue, the queue delays the execution of the barrier block (and any tasks submitted after the barrier) until all previously submitted tasks finish executing. After the previous tasks finish executing, the queue executes the barrier block by itself. Once the barrier block finishes, the queue resumes its normal execution behavior.

## See Also

- [class DispatchSemaphore](dispatchsemaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Semaphore](dispatch-semaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-barrier)*