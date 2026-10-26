# Dispatch Semaphore

**Framework**: Dispatch  
**Role**: API Collection

An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.

#### Overview

A dispatch semaphore is an efficient implementation of a traditional counting semaphore. Dispatch semaphores call down to the kernel only when the calling thread needs to be blocked. If the calling semaphore does not need to block, no kernel call is made.

You increment a semaphore count by calling the [`signal()`](./dispatchsemaphore/signal%28%29.md) method, and decrement a semaphore count by calling [`dispatch_semaphore_wait`](./dispatch_semaphore_wait.md) or one of its variants that specifies a timeout.

## Topics

### Creating a Semaphore
- [init(value: Int)](./dispatchsemaphore/init%28value%29.md)
  Creates new counting semaphore with an initial value.
- [typealias dispatch_semaphore_t](./dispatch_semaphore_t.md)
  A dispatch semaphore object.
- [OS_dispatch_semaphore](./os_dispatch_semaphore.md)
### Signaling the Semaphore
- [dispatch_semaphore_signal](./dispatch_semaphore_signal.md)
  Signals (increments) a semaphore.
### Blocking on the Semaphore
- [dispatch_semaphore_wait](./dispatch_semaphore_wait.md)
  Waits for (decrements) a semaphore.

## See Also

### Task Synchronization
- [class DispatchSemaphore](./dispatchsemaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](./dispatch-barrier.md)
  A synchronization point for tasks executing in a concurrent dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-semaphore)*