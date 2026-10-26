# Dispatch I/O

**Framework**: Dispatch  
**Role**: API Collection

An object that manages operations on a file descriptor using either stream-based or random-access semantics.

## Topics

### Creating a Dispatch I/O Object
- [typealias dispatch_io_t](./dispatch_io_t.md)
  A dispatch I/O channel.
- [dispatch_io_create](./dispatch_io_create.md)
  Creates a dispatch I/O channel and associates it with the specified file descriptor.
- [dispatch_io_create_with_io](./dispatch_io_create_with_io.md)
  Creates a new dispatch I/O channel from an existing channel.
- [dispatch_io_create_with_path](./dispatch_io_create_with_path.md)
  Creates a dispatch I/O channel with the associated path name.
- [dispatch_fd_t](./dispatch_fd_t.md)
  A file descriptor used for I/O operations.
- [OS_dispatch_io](./os_dispatch_io.md)
- [dispatch_io_type_t](./dispatch_io_type_t.md)
  The type of a dispatch I/O channel.
### Managing the File Descriptor
- [var fileDescriptor: Int32](./dispatchio/filedescriptor.md)
  Returns the file descriptor associated with the specified channel.
- [func setLimit(lowWater: Int)](./dispatchio/setlimit%28lowwater%29.md)
  Sets the minimum number of bytes to process before enqueueing a handler block.
- [func setLimit(highWater: Int)](./dispatchio/setlimit%28highwater%29.md)
  Sets the maximum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_interval](./dispatch_io_set_interval.md)
  Sets the interval (in nanoseconds) at which to invoke the I/O handlers for the channel.
- [dispatch_io_interval_flags_t](./dispatch_io_interval_flags_t.md)
  The desired delivery behavior for interval events.
### Synchronizing File Operations
- [func barrier(execute: () -> Void)](./dispatchio/barrier%28execute%29.md)
  Schedules a barrier operation on the specified channel.
### Reading from the File
- [dispatch_read](./dispatch_read.md)
  Schedules an asynchronous read operation using the specified file descriptor.
- [dispatch_io_read](./dispatch_io_read.md)
  Schedules an asynchronous read operation on the specified channel.
- [dispatch_io_handler_t](./dispatch_io_handler_t.md)
  A handler block used to process operations on a dispatch I/O channel.
### Writing to the File
- [dispatch_write](./dispatch_write.md)
  Schedules an asynchronous write operation using the specified file descriptor.
- [dispatch_io_write](./dispatch_io_write.md)
  Schedules an asynchronous write operation for the specified channel.
### Closing the File
- [dispatch_io_close](./dispatch_io_close.md)
  Closes the specified channel to new read and write operations.
- [dispatch_io_close_flags_t](./dispatch_io_close_flags_t.md)
  Additional flags to use when closing an I/O channel.

## See Also

### System Event Monitoring
- [class DispatchSource](./dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](./dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](./dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchData](./dispatchdata.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [struct DispatchDataIterator](./dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch Data](./dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](./dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch-i-o)*