# SetDataServicedHandler

**Framework**: DriverKit  
**Kind**: method

Installs the handler block to execute when data is removed from the queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetDataServicedHandler(OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

If your code produces data for the queue, use this method to install a handler so you can add more data to the queue. When space becomes available in the queue, the system executes your handler.

## Parameters

- `action`: The   object that contains the callback method to execute. The data queue retains your action object until you install a new handler or cancel the dispatch source. The system executes your callback on the dispatch queue you designated in your   object.

## See Also

- [DataServiced](iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.
- [Enqueue](iodataqueuedispatchsource/enqueue.md)
  Adds a single entry to the shared data queue.
- [EnqueueWithCoalesce](iodataqueuedispatchsource/enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn’t automatically send a data-available notification.
- [SendDataAvailable](iodataqueuedispatchsource/senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [IODataQueueClientEnqueueEntryBlock](iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/setdataservicedhandler)*