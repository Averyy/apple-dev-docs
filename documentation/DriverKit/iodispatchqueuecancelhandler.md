# IODispatchQueueCancelHandler

**Framework**: DriverKit  
**Kind**: typealias  
**Role**: Type Alias

A block to execute when a canceled dispatch queue stops executing tasks.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
typedef void (^)(void) IODispatchQueueCancelHandler;
```

## See Also

### Stopping the Queue
- [Cancel](./iodispatchqueue/cancel.md)
  Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueuecancelhandler)*