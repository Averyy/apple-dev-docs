# IODispatchFunction

**Framework**: DriverKit  
**Kind**: typealias

A C-style function to execute on a dispatch queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (*)(void *) IODispatchFunction;
```

## Parameters

- `context`: A pointer to contextual data that you need to perform any tasks. You specify the pointer to this data when scheduling the function for execution.

## See Also

- [DispatchAsync](iodispatchqueue/dispatchasync.md)
  Schedule a block for asynchronous execution on the current queue.
- [DispatchAsync_f](iodispatchqueue/dispatchasync_f.md)
  Schedule a C-style function for asynchrous execution on the current queue.
- [IODispatchBlock](iodispatchblock.md)
  A block to execute on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchfunction)*