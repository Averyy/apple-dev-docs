# DispatchSourceProtocol

**Framework**: Dispatch  
**Kind**: protocol

Defines a common set of properties and methods that are shared with all dispatch source types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol DispatchSourceProtocol : NSObjectProtocol
```

#### Overview

You do not adopt this protocol in your objects. Instead, use the [`makeSignalSource(signal:queue:)`](dispatchsource/makesignalsource(signal:queue:).md) method to create an object that adopts this protocol.

## Topics

### Activating, Suspending, and Resuming a Source
- [func activate()](dispatchsourceprotocol/activate.md)
  Activates the dispatch source.
- [func suspend()](dispatchsourceprotocol/suspend.md)
  Suspends the dispatch source.
- [func resume()](dispatchsourceprotocol/resume.md)
  Resumes the dispatch source.
### Canceling a Dispatch Source
- [func cancel()](dispatchsourceprotocol/cancel.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [var isCancelled: Bool](dispatchsourceprotocol/iscancelled.md)
  Returns a Boolean indicating whether the given dispatch source has been canceled.
- [func setCancelHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setcancelhandler(handler:).md)
  Sets the cancellation handler block for the dispatch source.
- [func setCancelHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setcancelhandler(qos:flags:handler:).md)
  Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.
### Installing Event Handlers
- [func setEventHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/seteventhandler(handler:).md)
  Sets the event handler work item for the dispatch source.
- [func setEventHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/seteventhandler(qos:flags:handler:).md)
- [func setRegistrationHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setregistrationhandler(handler:).md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:).md)
- [DispatchSourceProtocol.DispatchSourceHandler](dispatchsourceprotocol/dispatchsourcehandler.md)
### Getting the Dispatch Source Attributes
- [var handle: UInt](dispatchsourceprotocol/handle.md)
  Returns the underlying system handle associated with the specified dispatch source.
- [var data: UInt](dispatchsourceprotocol/data.md)
  Returns pending data for the dispatch source.
- [var mask: UInt](dispatchsourceprotocol/mask.md)
  Returns the mask of events monitored by the dispatch source.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
- [DispatchSourceMachReceive](dispatchsourcemachreceive.md)
- [DispatchSourceMachSend](dispatchsourcemachsend.md)
- [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)
- [DispatchSourceProcess](dispatchsourceprocess.md)
- [DispatchSourceRead](dispatchsourceread.md)
- [DispatchSourceSignal](dispatchsourcesignal.md)
- [DispatchSourceTimer](dispatchsourcetimer.md)
- [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md)
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md)
- [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md)
- [DispatchSourceWrite](dispatchsourcewrite.md)
### Conforming Types
- [DispatchSource](dispatchsource.md)

## See Also

- [class DispatchSource](dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchData](dispatchdata.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [struct DispatchDataIterator](dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol)*