# IsDataAvailable

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Checks whether the data queue contains data to process.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool IsDataAvailable();
```

## Return Value

`true` if the queue contains data to process, or `false` if it is empty.

## See Also

### Removing Work from the Queue
- [SetDataAvailableHandler](./setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [DataAvailable](./dataavailable.md)
  Responds to the addition of new data to the queue.
- [Peek](./peek.md)
  Returns the next queue entry without removing it from the queue.
- [Dequeue](./dequeue.md)
  Removes the next entry from the queue.
- [DequeueWithCoalesce](./dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn’t automatically send notifications.
- [SendDataServiced](./senddataserviced.md)
  Notifies interested parties that you removed data from the queue.
- [IODataQueueClientDequeueEntryBlock](../iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/isdataavailable)*