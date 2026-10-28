# SendDataServiced

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Notifies interested parties that you removed data from the queue.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
void SendDataServiced();
```

## Discussion

Use this method to send a single notification after dequeueing multiple entries with the [`DequeueWithCoalesce`](./dequeuewithcoalesce.md) method. The [`DequeueWithCoalesce`](./dequeuewithcoalesce.md) method doesn’t call the [`DataServiced`](./dataserviced.md) handler automatically after removing an entry. Instead, you call this method after the successful removal of entries from the queue.

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
- [Dequeue](./dequeue.md)
  Removes the next entry from the queue.
- [DequeueWithCoalesce](./dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn’t automatically send notifications.
- [IODataQueueClientDequeueEntryBlock](../iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/senddataserviced)*