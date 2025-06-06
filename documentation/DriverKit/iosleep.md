# IOSleep

**Framework**: DriverKit  
**Kind**: func

Sleep the calling thread for a number of milliseconds.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void IOSleep(uint64_t ms);
```

#### Discussion

This function blocks the calling thread for at least the number of specified milliseconds, giving time to other processes.

## Parameters

- `ms`: The integer number of milliseconds to wait.

## See Also

- [IODelay](iodelay.md)
  Sleep the calling thread for a number of microseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iosleep)*