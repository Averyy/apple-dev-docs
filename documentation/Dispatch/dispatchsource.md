# DispatchSource

**Framework**: Dispatch  
**Kind**: class

An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.

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
class DispatchSource
```

#### Overview

Use the methods of this class to construct new dispatch sources of the appropriate types.

## Topics

### Managing Common Dispatch Source Properties
- [protocol DispatchSourceProtocol](dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.
### Creating a Timer Source
- [class func makeTimerSource(flags: DispatchSource.TimerFlags, queue: DispatchQueue?) -> any DispatchSourceTimer](dispatchsource/maketimersource(flags:queue:).md)
  Creates a new dispatch source object for monitoring timer events.
- [protocol DispatchSourceTimer](dispatchsourcetimer.md)
  A dispatch source that submits the event handler block based on a timer.
- [DispatchSource.TimerFlags](dispatchsource/timerflags.md)
  Flags to use when configuring a timer dispatch source.
### Creating a File System Source
- [class func makeReadSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceRead](dispatchsource/makereadsource(filedescriptor:queue:).md)
  Creates a new dispatch source object for reading bytes from the specified file.
- [class func makeWriteSource(fileDescriptor: Int32, queue: DispatchQueue?) -> any DispatchSourceWrite](dispatchsource/makewritesource(filedescriptor:queue:).md)
  Creates a new dispatch source object for writing data to the specified file.
- [class func makeFileSystemObjectSource(fileDescriptor: Int32, eventMask: DispatchSource.FileSystemEvent, queue: DispatchQueue?) -> any DispatchSourceFileSystemObject](dispatchsource/makefilesystemobjectsource(filedescriptor:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring file-system events.
- [protocol DispatchSourceRead](dispatchsourceread.md)
  A dispatch source object for reading data from a file descriptor.
- [protocol DispatchSourceWrite](dispatchsourcewrite.md)
  A dispatch source object for writing data to a file descriptor.
- [protocol DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
  A dispatch source that monitors events associated with a file descriptor.
- [DispatchSource.FileSystemEvent](dispatchsource/filesystemevent.md)
  Events involving a change to a file system object.
### Creating a Process Source
- [class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue?) -> any DispatchSourceProcess](dispatchsource/makeprocesssource(identifier:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring the specified process.
- [protocol DispatchSourceProcess](dispatchsourceprocess.md)
  A dispatch source that monitors an external process for events.
- [DispatchSource.ProcessEvent](dispatchsource/processevent.md)
  Events related to a process.
### Creating a Memory Pressure Source
- [class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue?) -> any DispatchSourceMemoryPressure](dispatchsource/makememorypressuresource(eventmask:queue:).md)
  Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [protocol DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)
  A dispatch source that monitors the system for changes in the memory pressure condition.
- [DispatchSource.MemoryPressureEvent](dispatchsource/memorypressureevent.md)
  Memory pressure events.
### Creating a Signal Source
- [class func makeSignalSource(signal: Int32, queue: DispatchQueue?) -> any DispatchSourceSignal](dispatchsource/makesignalsource(signal:queue:).md)
  Creates a new dispatch source object that monitors the arrival of a UNIX signal.
- [protocol DispatchSourceSignal](dispatchsourcesignal.md)
  A dispatch source that monitors the current process for UNIX signals.
### Creating a Mach Port Source
- [class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue?) -> any DispatchSourceMachReceive](dispatchsource/makemachreceivesource(port:queue:).md)
  Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue?) -> any DispatchSourceMachSend](dispatchsource/makemachsendsource(port:eventmask:queue:).md)
  A dispatch source that monitors a Mach port for dead name notifications.
- [protocol DispatchSourceMachReceive](dispatchsourcemachreceive.md)
  A dispatch source that monitors a Mach port for pending messages.
- [protocol DispatchSourceMachSend](dispatchsourcemachsend.md)
  A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [DispatchSource.MachSendEvent](dispatchsource/machsendevent.md)
  Mach-related events.
### Creating a Custom Source
- [class func makeUserDataAddSource(queue: DispatchQueue?) -> any DispatchSourceUserDataAdd](dispatchsource/makeuserdataaddsource(queue:).md)
  Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [class func makeUserDataOrSource(queue: DispatchQueue?) -> any DispatchSourceUserDataOr](dispatchsource/makeuserdataorsource(queue:).md)
  Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [class func makeUserDataReplaceSource(queue: DispatchQueue?) -> any DispatchSourceUserDataReplace](dispatchsource/makeuserdatareplacesource(queue:).md)
  Creates a new dispatch source object that you use to track custom app data.
- [protocol DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md)
  A dispatch source that coalesces data you provide using an AND operation.
- [protocol DispatchSourceUserDataOr](dispatchsourceuserdataor.md)
  A dispatch source that coalesces data you provide using an OR operation.
- [protocol DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md)
  A dispatch source that replaces any pending data with the new value you provide.

## Relationships

### Inherits From
- [DispatchObject](dispatchobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md)
- [DispatchSourceMachReceive](dispatchsourcemachreceive.md)
- [DispatchSourceMachSend](dispatchsourcemachsend.md)
- [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md)
- [DispatchSourceProcess](dispatchsourceprocess.md)
- [DispatchSourceProtocol](dispatchsourceprotocol.md)
- [DispatchSourceRead](dispatchsourceread.md)
- [DispatchSourceSignal](dispatchsourcesignal.md)
- [DispatchSourceTimer](dispatchsourcetimer.md)
- [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md)
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md)
- [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md)
- [DispatchSourceWrite](dispatchsourcewrite.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [protocol DispatchSourceProtocol](dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource)*