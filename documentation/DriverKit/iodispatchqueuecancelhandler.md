# IODispatchQueueCancelHandler

**Framework**: DriverKit  
**Kind**: typealias

A block to execute when a canceled dispatch queue stops executing tasks.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(void) IODispatchQueueCancelHandler;
```

## See Also

- [Cancel](iodispatchqueue/cancel.md)
  Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueuecancelhandler)*