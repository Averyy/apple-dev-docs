# IOLogv

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
int IOLogv(const char * format, va_list ap);
```

#### Discussion

Log a message to console in text mode, and os_log.

This function allows a driver to log diagnostic information to the screen during verbose boots, and to os_log.

## Parameters

- `format`: A printf() style format string (see printf(3) documentation).
- `ap`: stdarg(3) style variable arguments.

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
- [IOLockAlloc](iolockalloc.md)
- [IOLockAssert](iolockassert.md)
- [IOLockFree](iolockfree.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iologv)*