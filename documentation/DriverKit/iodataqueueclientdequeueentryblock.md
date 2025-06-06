# IODataQueueClientDequeueEntryBlock

**Framework**: DriverKit  
**Kind**: typealias

The handler block you use to remove data from a queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(const void *, unsigned long) IODataQueueClientDequeueEntryBlock;
```

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
- [SendDataServiced](iodataqueuedispatchsource/senddataserviced.md)
  Notifies interested parties that you removed data from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueueclientdequeueentryblock)*