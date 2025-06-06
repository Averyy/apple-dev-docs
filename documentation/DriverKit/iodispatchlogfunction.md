# IODispatchLogFunction

**Framework**: DriverKit  
**Kind**: typealias

A function that logs content.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef int (*)(const char *, ...) IODispatchLogFunction;
```

## Parameters

- `format`: The C string to add to the log.

## See Also

- [Log](iodispatchqueue/log.md)
  Log the current execution context with respect to any queues the current thread holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchlogfunction)*