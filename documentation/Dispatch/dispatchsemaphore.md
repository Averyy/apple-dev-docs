# DispatchSemaphore

**Framework**: Dispatch  
**Kind**: class  
**Role**: Class

An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class DispatchSemaphore
```

#### Overview

A dispatch semaphore is an efficient implementation of a traditional counting semaphore. Dispatch semaphores call down to the kernel only when the calling thread needs to be blocked. If the calling semaphore does not need to block, no kernel call is made.

You increment a semaphore count by calling the [`signal()`](./dispatchsemaphore/signal%28%29.md) method, and decrement a semaphore count by calling [`wait()`](./dispatchsemaphore/wait%28%29.md) or one of its variants that specifies a timeout.

## Topics

### Creating a Semaphore
- [init(value: Int)](./dispatchsemaphore/init%28value%29.md)
  Creates new counting semaphore with an initial value.
### Signaling the Semaphore
- [func signal() -> Int](./dispatchsemaphore/signal%28%29.md)
  Signals (increments) a semaphore.
### Blocking on the Semaphore
- [func wait()](./dispatchsemaphore/wait%28%29.md)
  Waits for, or decrements, a semaphore.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](./dispatchsemaphore/wait%28timeout%29.md)
  Waits for, or decrements, a semaphore.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](./dispatchsemaphore/wait%28walltimeout%29.md)
  Waits for, or decrements, a semaphore.

## Relationships

### Inherits From
- [DispatchObject](./dispatchobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Task Synchronization
- [Dispatch Semaphore](./dispatch-semaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](./dispatch-barrier.md)
  A synchronization point for tasks executing in a concurrent dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore)*