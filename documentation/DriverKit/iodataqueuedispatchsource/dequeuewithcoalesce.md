# DequeueWithCoalesce

**Framework**: DriverKit  
**Kind**: method

Removes the next queue entry, but doesn’t automatically send notifications.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t DequeueWithCoalesce(bool * sendDataServiced, IODataQueueClientDequeueEntryBlockcallback);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, [`kIOReturnUnderrun`](kioreturnunderrun.md) if the queue is empty, or [`kIOReturnError`](kioreturnerror.md) if the queue is corrupt. See [`Error Codes`](error-codes.md).

## Parameters

- `sendDataServiced`: A Boolean value that indicates that this method would have sent a notification. Initialize the value to  , and then make one or more calls to this method. If the value is   after all of those calls, call the   method yourself to deliver the notification.
- `callback`: The callback that you use to process the dequeued data.

## See Also

- [SetDataAvailableHandler](iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [DataAvailable](iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue.
- [IsDataAvailable](iodataqueuedispatchsource/isdataavailable.md)
  Checks whether the data queue contains data to process.
- [Peek](iodataqueuedispatchsource/peek.md)
  Returns the next queue entry without removing it from the queue.
- [Dequeue](iodataqueuedispatchsource/dequeue.md)
  Removes the next entry from the queue.
- [SendDataServiced](iodataqueuedispatchsource/senddataserviced.md)
  Notifies interested parties that you removed data from the queue.
- [IODataQueueClientDequeueEntryBlock](iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dequeuewithcoalesce)*