# IOTimerDispatchSource

**Framework**: DriverKit  
**Kind**: class

A dispatch source that notifies your driver at a specific time.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOTimerDispatchSource;
```

#### Overview

An [`IOTimerDispatchSource`](iotimerdispatchsource.md) object executes an associated action at a designated time. After configuring the dispatch source object, call the [`WakeAtTime`](iotimerdispatchsource/wakeattime.md) method to schedule the time at which to execute your code. There are several timebases you can use to configure the timer, but the most common one is [`kIOTimerClockMachAbsoluteTime`](kiotimerclockmachabsolutetime.md).

## Topics

### Configuring the Timer Source
- [Create](iotimerdispatchsource/create.md)
  Creates and configures a timer dispatch object.
- [init](iotimerdispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iotimerdispatchsource/free.md)
  Performs any final cleanup for the timer dispatch source.
- [SetHandler](iotimerdispatchsource/sethandler.md)
  Sets the handler block to run when the timer fires.
### Rescheduling the Timer
- [WakeAtTime](iotimerdispatchsource/wakeattime.md)
  Schedules a callback from the timer.
- [Clock Types](3242783-clock_types.md)
  Clock types to use when configuring a timer.
### Starting and Stopping the Timer Source
- [SetEnableWithCompletion](iotimerdispatchsource/setenablewithcompletion.md)
  Enables or disables the timer.
- [Cancel](iotimerdispatchsource/cancel.md)
  Cancels all callbacks from the event source.
### Declaring Actions
- [TimerOccurred](iotimerdispatchsource/timeroccurred.md)
  Executes custom code when the timer fires.
- [CheckForWork](iotimerdispatchsource/checkforwork.md)
  Checks for events to handle.

## Relationships

### Inherits From
- [IODispatchSource](iodispatchsource.md)

## See Also

- [IODispatchQueue](iodispatchqueue.md)
  An object that manages the serial execution of blocks.
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
  A dispatch source that reports hardware-related interrupt events to your driver.
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
  A dispatch source that manages a shared-memory data queue.
- [IODispatchSource](iodispatchsource.md)
  The common base class for dispatch sources.
- [OSAction](osaction.md)
  An object that executes your driver’s custom behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource)*