# DispatchSemaphore

**Framework**: Dispatch  
**Kind**: class

An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class DispatchSemaphore
```

#### Overview

A dispatch semaphore is an efficient implementation of a traditional counting semaphore. Dispatch semaphores call down to the kernel only when the calling thread needs to be blocked. If the calling semaphore does not need to block, no kernel call is made.

You increment a semaphore count by calling the [`signal()`](dispatchsemaphore/signal().md) method, and decrement a semaphore count by calling [`wait()`](dispatchsemaphore/wait().md) or one of its variants that specifies a timeout.

## Topics

### Creating a Semaphore
- [init(value: Int)](dispatchsemaphore/init(value:).md)
  Creates new counting semaphore with an initial value.
### Signaling the Semaphore
- [func signal() -> Int](dispatchsemaphore/signal.md)
  Signals (increments) a semaphore.
### Blocking on the Semaphore
- [func wait()](dispatchsemaphore/wait.md)
  Waits for, or decrements, a semaphore.
- [func wait(timeout: DispatchTime) -> DispatchTimeoutResult](dispatchsemaphore/wait(timeout:).md)
  Waits for, or decrements, a semaphore.
- [func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult](dispatchsemaphore/wait(walltimeout:).md)
  Waits for, or decrements, a semaphore.

## Relationships

### Inherits From
- [DispatchObject](dispatchobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Dispatch Semaphore](dispatch-semaphore.md)
  An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](dispatch-barrier.md)
  A synchronization point for tasks executing in a concurrent dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsemaphore)*