# DispatchIO

**Framework**: Dispatch  
**Kind**: class

An object that manages operations on a file descriptor using either stream-based or random-access semantics.

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
class DispatchIO
```

## Topics

### Creating a Dispatch I/O Object
- [convenience init(type: DispatchIO.StreamType, fileDescriptor: Int32, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:filedescriptor:queue:cleanuphandler:).md)
  Creates a new I/O channel that accesses the specified file descriptor.
- [convenience init?(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-50rb0.md)
  Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [convenience init(type: DispatchIO.StreamType, io: DispatchIO, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:io:queue:cleanuphandler:).md)
  Creates a new I/O channel from an existing I/O channel.
- [DispatchIO.StreamType](dispatchio/streamtype.md)
  The semantics for accessing the contents of a file descriptor.
### Reading from the File
- [func read(offset: off_t, length: Int, queue: DispatchQueue, ioHandler: (Bool, DispatchData?, Int32) -> Void)](dispatchio/read(offset:length:queue:iohandler:).md)
  Schedules an asynchronous read operation on the specified channel.
- [class func read(fromFileDescriptor: Int32, maxLength: Int, runningHandlerOn: DispatchQueue, handler: (DispatchData, Int32) -> Void)](dispatchio/read(fromfiledescriptor:maxlength:runninghandleron:handler:).md)
  Schedules an asynchronous read operation using the specified file descriptor.
### Writing to the File
- [func write(offset: off_t, data: DispatchData, queue: DispatchQueue, ioHandler: (Bool, DispatchData?, Int32) -> Void)](dispatchio/write(offset:data:queue:iohandler:).md)
  Schedules an asynchronous write operation for the specified channel.
- [class func write(toFileDescriptor: Int32, data: DispatchData, runningHandlerOn: DispatchQueue, handler: (DispatchData?, Int32) -> Void)](dispatchio/write(tofiledescriptor:data:runninghandleron:handler:).md)
  Schedules an asynchronous write operation to the specified file descriptor.
### Closing the File
- [func close(flags: DispatchIO.CloseFlags)](dispatchio/close(flags:).md)
  Closes the channel to new read and write operations.
- [DispatchIO.CloseFlags](dispatchio/closeflags.md)
  Additional flags to use when closing an I/O channel.
### Managing the File Descriptor
- [var fileDescriptor: Int32](dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(highWater: Int)](dispatchio/setlimit(highwater:).md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [func setLimit(lowWater: Int)](dispatchio/setlimit(lowwater:).md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setInterval(interval: DispatchTimeInterval, flags: DispatchIO.IntervalFlags)](dispatchio/setinterval(interval:flags:).md)
  Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [DispatchIO.IntervalFlags](dispatchio/intervalflags.md)
  The desired delivery behavior for interval events.
### Synchronizing File Operations
- [func barrier(execute: () -> Void)](dispatchio/barrier(execute:).md)
  Schedules a barrier operation on the specified channel.
### Initializers
- [convenience init(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: (Int32) -> Void)](dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-25rlb.md)

## Relationships

### Inherits From
- [DispatchObject](dispatchobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class DispatchSource](dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio)*