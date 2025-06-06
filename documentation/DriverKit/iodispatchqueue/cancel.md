# Cancel

**Framework**: DriverKit  
**Kind**: method

Stops the queue from dequeueing any further tasks, and notifies the specified handler when all in-flight tasks finish.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Cancel(IODispatchQueueCancelHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

This method asynchronously tells the dispatch queue to stop the execution of queued tasks, and returns immediately. If a task is already executing, that task runs to completion. After all tasks finish, the dispatch queue executes the block in the `handler` parameter.

## Parameters

- `handler`: The block to execute when the queue finishes all in-flight work.

## See Also

- [IODispatchQueueCancelHandler](iodispatchqueuecancelhandler.md)
  A block to execute when a canceled dispatch queue stops executing tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/cancel)*