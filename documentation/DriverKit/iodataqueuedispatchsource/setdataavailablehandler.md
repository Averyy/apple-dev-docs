# SetDataAvailableHandler

**Framework**: DriverKit  
**Kind**: method

Sets the handler block to run when another object adds data to the queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetDataAvailableHandler(OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `action`: The   instance specifying the callback method. The data queue retains this object until you call this method again or call  . This queue executes the action’s handler method on the action’s own dispatch queue.

## See Also

- [DataAvailable](iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue.
- [IsDataAvailable](iodataqueuedispatchsource/isdataavailable.md)
  Checks whether the data queue contains data to process.
- [Peek](iodataqueuedispatchsource/peek.md)
  Returns the next queue entry without removing it from the queue.
- [Dequeue](iodataqueuedispatchsource/dequeue.md)
  Removes the next entry from the queue.
- [DequeueWithCoalesce](iodataqueuedispatchsource/dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn’t automatically send notifications.
- [SendDataServiced](iodataqueuedispatchsource/senddataserviced.md)
  Notifies interested parties that you removed data from the queue.
- [IODataQueueClientDequeueEntryBlock](iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/setdataavailablehandler)*