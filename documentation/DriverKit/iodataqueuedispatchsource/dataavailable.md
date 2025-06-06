# DataAvailable

**Framework**: DriverKit  
**Kind**: method

Responds to the addition of new data to the queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void DataAvailable(OSAction * action);
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

Use this method as a prototype for declaring your own custom data-queue handlers. When declaring your method, use the [`TYPE`](type.md) macro to indicate that your method has the same parameters and return value as this method.

Use the implementation of your method to examine the data in the queue and remove it when appropriate.

## Parameters

- `action`: The action object being executed.

## See Also

- [SetDataAvailableHandler](iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dataavailable)*