# IODispatchBlock

**Framework**: DriverKit  
**Kind**: typealias

A block to execute on a dispatch queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(void) IODispatchBlock;
```

## See Also

- [DispatchAsync](iodispatchqueue/dispatchasync.md)
  Schedule a block for asynchronous execution on the current queue.
- [DispatchAsync_f](iodispatchqueue/dispatchasync_f.md)
  Schedule a C-style function for asynchrous execution on the current queue.
- [IODispatchFunction](iodispatchfunction.md)
  A C-style function to execute on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchblock)*