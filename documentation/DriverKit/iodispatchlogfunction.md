# IODispatchLogFunction

**Framework**: DriverKit  
**Kind**: typealias  
**Role**: Type Alias

A function that logs content.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
typedef int (*)(const char *, ...) IODispatchLogFunction;
```

## Parameters

- `format`: The C string to add to the log.

## See Also

### Logging Dispatch Information
- [Log](./iodispatchqueue/log.md)
  Log the current execution context with respect to any queues the current thread holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchlogfunction)*