# Log

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Log the current execution context with respect to any queues the current thread holds.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static void Log(const char *message, IODispatchLogFunction output);
```

## Parameters

- `message`: A C string that contains the message to add to the log file.
- `output`: The function address to use for logging the content. The address of [`IOLog`](../iolog.md) is suitable for use.

## See Also

### Logging Dispatch Information
- [IODispatchLogFunction](../iodispatchlogfunction.md)
  A function that logs content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/log)*