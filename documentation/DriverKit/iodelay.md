# IODelay

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function

Sleep the calling thread for a number of microseconds.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
void IODelay(uint64_t us);
```

#### Discussion

This function blocks the calling thread for at least the number of specified microseconds, giving time to other processes.

## Parameters

- `us`: The integer number of microseconds to wait.

## See Also

### Thread Utilities
- [IOSleep](./iosleep.md)
  Sleep the calling thread for a number of milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodelay)*