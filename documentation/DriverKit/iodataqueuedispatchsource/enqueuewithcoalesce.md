# EnqueueWithCoalesce

**Framework**: DriverKit  
**Kind**: method

Adds an entry to the queue, but doesn’t automatically send a data-available notification.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t EnqueueWithCoalesce(uint32_t dataSize, bool * sendDataAvailable, IODataQueueClientEnqueueEntryBlockcallback);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, [`kIOReturnOverrun`](kioreturnoverrun.md) if the queue was full, or [`kIOReturnError`](kioreturnerror.md) if the queue is corrupt. See [`Error Codes`](error-codes.md).

## Parameters

- `dataSize`: The size of the data to enqueue.
- `sendDataAvailable`: A Boolean value that indicates that this method would have sent a notification. Initialize the value to  , and then make one or more calls to this method. If the value is   after all of those calls, call the   method yourself to deliver the notification.
- `callback`: The callback to execute when there is enough space to enqueue the data.

## See Also

- [SetDataServicedHandler](iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [DataServiced](iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.
- [Enqueue](iodataqueuedispatchsource/enqueue.md)
  Adds a single entry to the shared data queue.
- [SendDataAvailable](iodataqueuedispatchsource/senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [IODataQueueClientEnqueueEntryBlock](iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/enqueuewithcoalesce)*