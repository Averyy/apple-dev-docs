# IODataQueueDispatchSource

**Framework**: DriverKit  
**Kind**: class

A dispatch source that manages a shared-memory data queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IODataQueueDispatchSource;
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

## Topics

### Configuring the Dispatch Source
- [Create](iodataqueuedispatchsource/create.md)
  Creates a dispatch source that you use as a shared-memory data queue.
- [init](iodataqueuedispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iodataqueuedispatchsource/free.md)
  Performs any final cleanup for the data-queue dispatch source.
### Adding Work to the Queue
- [SetDataServicedHandler](iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
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
### Removing Work from the Queue
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
- [IODataQueueClientDequeueEntryBlock](iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.
### Starting and Stopping the Dispatch Source
- [SetEnableWithCompletion](iodataqueuedispatchsource/setenablewithcompletion.md)
  Controls the enable state of the interrupt source.
- [Cancel](iodataqueuedispatchsource/cancel.md)
  Cancels all callbacks from the dispatch source.
### Performing Internal Tasks
- [CopyDataAvailableHandler](iodataqueuedispatchsource/copydataavailablehandler.md)
  A private method that the dispatch source uses to detect enqueued data.
- [CopyDataServicedHandler](iodataqueuedispatchsource/copydataservicedhandler.md)
  A private method that the dispatch source uses to detect dequeued data.
- [CopyMemory](iodataqueuedispatchsource/copymemory.md)
  A private method that the dispatch source uses to copy memory.
- [CheckForWork](iodataqueuedispatchsource/checkforwork.md)
  Checks for events to handle.
### Instance Methods
- [CanEnqueueData](iodataqueuedispatchsource/canenqueuedata-4tug8.md)
- [CanEnqueueData](iodataqueuedispatchsource/canenqueuedata-3yyz2.md)
### Type Methods
- [GetDataQueueEntryHeaderSize](iodataqueuedispatchsource/getdataqueueentryheadersize.md)

## Relationships

### Inherits From
- [IODispatchSource](iodispatchsource.md)

## See Also

- [IODispatchQueue](iodispatchqueue.md)
  An object that manages the serial execution of blocks.
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
  A dispatch source that reports hardware-related interrupt events to your driver.
- [IOTimerDispatchSource](iotimerdispatchsource.md)
  A dispatch source that notifies your driver at a specific time.
- [IODispatchSource](iodispatchsource.md)
  The common base class for dispatch sources.
- [OSAction](osaction.md)
  An object that executes your driver’s custom behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource)*