# DataServiced

**Framework**: DriverKit  
**Kind**: method

Responds to the removal of data from the queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void DataServiced(OSAction * action);
```

#### Discussion

Use this method as a prototype for declaring your own custom data-queue handler. When declaring your method, use the [`TYPE`](type.md) macro to indicate that your method has the same parameters and return value as this method.

Use the implementation of your method to add more data to the queue or perform other relevant tasks.

## Parameters

- `action`: The action object being executed.

## See Also

- [SetDataServicedHandler](iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [Enqueue](iodataqueuedispatchsource/enqueue.md)
  Adds a single entry to the shared data queue.
- [EnqueueWithCoalesce](iodataqueuedispatchsource/enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn’t automatically send a data-available notification.
- [SendDataAvailable](iodataqueuedispatchsource/senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [IODataQueueClientEnqueueEntryBlock](iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dataserviced)*