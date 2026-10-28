# DispatchSync

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Schedule a block for synchronous execution on the current queue.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
void DispatchSync(IODispatchBlock block);
```

## Discussion

This method schedules the block for execution on the queue and waits for it to complete before returning. The system retains the queue until the block completes.

## Parameters

- `block`: The block to execute on the queue.

## See Also

### Executing a Task Synchronously
- [DispatchSync_f](./dispatchsync_f.md)
  Schedule a C-style function for synchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/dispatchsync)*