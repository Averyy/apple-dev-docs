# SendDataServiced

**Framework**: DriverKit  
**Kind**: method

Notifies interested parties that you removed data from the queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void SendDataServiced();
```

#### Discussion

Use this method to send a single notification after dequeueing multiple entries with the [`DequeueWithCoalesce`](iodataqueuedispatchsource/dequeuewithcoalesce.md) method. The [`DequeueWithCoalesce`](iodataqueuedispatchsource/dequeuewithcoalesce.md) method doesn’t call the [`DataServiced`](iodataqueuedispatchsource/dataserviced.md) handler automatically after removing an entry. Instead, you call this method after the successful removal of entries from the queue.

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
- [DequeueWithCoalesce](iodataqueuedispatchsource/dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn’t automatically send notifications.
- [IODataQueueClientDequeueEntryBlock](iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/senddataserviced)*