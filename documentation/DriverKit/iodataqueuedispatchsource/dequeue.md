# Dequeue

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Removes the next entry from the queue.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
kern_return_t Dequeue(IODataQueueClientDequeueEntryBlock callback);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, [`kIOReturnUnderrun`](../kioreturnunderrun.md) if the queue is empty, or [`kIOReturnError`](../kioreturnerror.md) if the queue is corrupt. See [Error Codes](../error-codes.md).

## Parameters

- `callback`: The callback you use to process the next entry in the queue.

## See Also

### Removing Work from the Queue
- [SetDataAvailableHandler](./setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [DataAvailable](./dataavailable.md)
  Responds to the addition of new data to the queue.
- [IsDataAvailable](./isdataavailable.md)
  Checks whether the data queue contains data to process.
- [Peek](./peek.md)
  Returns the next queue entry without removing it from the queue.
- [DequeueWithCoalesce](./dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn’t automatically send notifications.
- [SendDataServiced](./senddataserviced.md)
  Notifies interested parties that you removed data from the queue.
- [IODataQueueClientDequeueEntryBlock](../iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dequeue)*