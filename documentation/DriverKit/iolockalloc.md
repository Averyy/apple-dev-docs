# IOLockAlloc

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
struct IOLock * IOLockAlloc();
```

#### Return Value

Pointer to the allocated lock, or zero on failure.

#### Discussion

Allocates a mutex in general purpose memory, and initializes it.

## See Also

- [dequeue_head](dequeue_head.md)
- [dequeue_tail](dequeue_tail.md)
- [enqueue_head](enqueue_head.md)
- [enqueue_tail](enqueue_tail.md)
- [get_IOHistogramReporter_IVars](get_iohistogramreporter_ivars-4lwpg.md)
- [get_IOHistogramReporter_IVars](get_iohistogramreporter_ivars-5lkdv.md)
- [get_IOReporter_IVars](get_ioreporter_ivars-6q8vt.md)
- [get_IOReporter_IVars](get_ioreporter_ivars-89ntc.md)
- [get_IOStateReporter_IVars](get_iostatereporter_ivars-3g28i.md)
- [get_IOStateReporter_IVars](get_iostatereporter_ivars-56435.md)
- [insque](insque.md)
- [IOCallOnce](iocallonce.md)
- [IOLockAssert](iolockassert.md)
- [IOLockFree](iolockfree.md)
- [IOLockLock](iolocklock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iolockalloc)*