# DispatchSync

**Framework**: DriverKit  
**Kind**: method

Schedule a block for synchronous execution on the current queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void DispatchSync(IODispatchBlockblock);
```

#### Discussion

This method schedules the block for execution on the queue and waits for it to complete before returning. The system retains the queue until the block completes.

## Parameters

- `block`: The block to execute on the queue.

## See Also

- [DispatchSync_f](iodispatchqueue/dispatchsync_f.md)
  Schedule a C-style function for synchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/dispatchsync)*