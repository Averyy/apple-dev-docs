# DispatchSync_f

**Framework**: DriverKit  
**Kind**: method

Schedule a C-style function for synchronous execution on the current queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void DispatchSync_f(void * context, IODispatchFunction function);
```

#### Discussion

This method schedules the function for execution on the queue and waits for it to complete before returning. The system retains the queue until the function completes.

## Parameters

- `context`: A pointer to contextual data that you want to pass to the function.
- `function`: The function to execute on the queue.

## See Also

- [DispatchSync](iodispatchqueue/dispatchsync.md)
  Schedule a block for synchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/dispatchsync_f)*