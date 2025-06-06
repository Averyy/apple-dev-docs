# IODispatchSource

**Framework**: DriverKit  
**Kind**: class

The common base class for dispatch sources.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IODispatchSource;
```

## Topics

### Configuring the Dispatch Source
- [init](iodispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iodispatchsource/free.md)
  Performs any final cleanup for the dispatch source.
- [Cancel](iodispatchsource/cancel.md)
  Cancel all callbacks from the dispatch source.
### Enabling and Disabling the Source
- [SetEnable](iodispatchsource/setenable.md)
  Enables or disables the delivery of events to your code.
- [SetEnableWithCompletion](iodispatchsource/setenablewithcompletion.md)
  Enables or disables the dispatch source.
### Checking the State of the Source
- [CheckForWork](iodispatchsource/checkforwork.md)
  Checks for events to handle.

## Relationships

### Inherits From
- [OSObject](osobject.md)
### Inherited By
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
- [IOServiceNotificationDispatchSource](ioservicenotificationdispatchsource.md)
- [IOServiceStateNotificationDispatchSource](ioservicestatenotificationdispatchsource.md)
- [IOTimerDispatchSource](iotimerdispatchsource.md)

## See Also

- [IODispatchQueue](iodispatchqueue.md)
  An object that manages the serial execution of blocks.
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
  A dispatch source that reports hardware-related interrupt events to your driver.
- [IOTimerDispatchSource](iotimerdispatchsource.md)
  A dispatch source that notifies your driver at a specific time.
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
  A dispatch source that manages a shared-memory data queue.
- [OSAction](osaction.md)
  An object that executes your driver’s custom behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource)*