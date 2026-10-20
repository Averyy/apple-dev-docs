# SendDataAvailable

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Sends a notification to observers that indicates more data is available for processing.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
void SendDataAvailable();
```

## See Also

### Adding Work to the Queue
- [SetDataServicedHandler](./setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [DataServiced](./dataserviced.md)
  Responds to the removal of data from the queue.
- [Enqueue](./enqueue.md)
  Adds a single entry to the shared data queue.
- [EnqueueWithCoalesce](./enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn’t automatically send a data-available notification.
- [IODataQueueClientEnqueueEntryBlock](../iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/senddataavailable)*