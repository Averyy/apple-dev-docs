# Log

**Framework**: DriverKit  
**Kind**: method

Log the current execution context with respect to any queues the current thread holds.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static void Log(const char * message, IODispatchLogFunction output);
```

## Parameters

- `message`: A C string that contains the message to add to the log file.
- `output`: The function address to use for logging the content. The address of   is suitable for use.

## See Also

- [IODispatchLogFunction](iodispatchlogfunction.md)
  A function that logs content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/log)*