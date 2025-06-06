# Dispatch I/O

**Framework**: Dispatch

An object that manages operations on a file descriptor using either stream-based or random-access semantics.

## Topics

### Creating a Dispatch I/O Object
- [typealias dispatch_io_t](dispatch_io_t.md)
  A dispatch I/O channel.
### Managing the File Descriptor
- [var fileDescriptor: Int32](dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(lowWater: Int)](dispatchio/setlimit(lowwater:).md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setLimit(highWater: Int)](dispatchio/setlimit(highwater:).md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
### Synchronizing File Operations
- [func barrier(execute: () -> Void)](dispatchio/barrier(execute:).md)
  Schedules a barrier operation on the specified channel.

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
- [Dispatch Data](dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-i-o)*