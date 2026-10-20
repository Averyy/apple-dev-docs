# DataAvailable

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Responds to the addition of new data to the queue.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual void DataAvailable(OSAction *action);
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](../creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

Use this method as a prototype for declaring your own custom data-queue handlers. When declaring your method, use the [`TYPE`](../type.md) macro to indicate that your method has the same parameters and return value as this method.

Use the implementation of your method to examine the data in the queue and remove it when appropriate.

## Parameters

- `action`: The action object being executed.

## See Also

### Removing Work from the Queue
- [SetDataAvailableHandler](./setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [IsDataAvailable](./isdataavailable.md)
  Checks whether the data queue contains data to process.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dataavailable)*