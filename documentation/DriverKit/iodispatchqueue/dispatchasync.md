# DispatchAsync

**Framework**: DriverKit  
**Kind**: method

Schedule a block for asynchronous execution on the current queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void DispatchAsync(IODispatchBlockblock);
```

#### Discussion

This method schedules the block for execution on the queue and returns immediately, without waiting for execution of the block to begin. The system retains the queue until the block completes.

## Parameters

- `block`: The block to execute on the queue.

## See Also

- [DispatchAsync_f](iodispatchqueue/dispatchasync_f.md)
  Schedule a C-style function for asynchrous execution on the current queue.
- [IODispatchBlock](iodispatchblock.md)
  A block to execute on a dispatch queue.
- [IODispatchFunction](iodispatchfunction.md)
  A C-style function to execute on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/dispatchasync)*