# dispatch_read

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules an asynchronous read operation using the specified file descriptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_read(dispatch_fd_t fd, size_t length, dispatch_queue_t queue, void (^handler)(dispatch_data_t data, int error));
```

#### Discussion

This is a convenience function for initiating a single, asynchronous read operation from the current position of the specified file descriptor. This method is intended for simple operations where you do not need the overhead of creating a channel and do not plan on issuing more than a few calls to read or write data. Once submitted, there is no way to cancel the read operation.

After calling this function, the system takes control of the specified file descriptor until the handler block is enqueued. While it controls the file descriptor, the system may modify it on behalf of the application. For example, the system typically adds the `O_NONBLOCK` flag to ensure that any operations are non-blocking. During that time, it is an error for your application to modify the file descriptor directly. However, you may pass the file descriptor to this function or the [`dispatch_write`](./dispatch_write.md) function to perform additional reads or writes. You may also use the file descriptor to create a new dispatch I/O channel.

The `handler` you provide is not queued for execution until the read operation finishes. In addition, if you issue multiple read or write calls for the same file descriptor using the convenience APIs, all of those operations must complete before any of the associated handlers are queued. If you are already using the file descriptor with another channel, you should use the [`read(offset:length:queue:ioHandler:)`](./dispatchio/read%28offset,length,queue,iohandler%29.md) function to read data from the channel rather than use this function.

If you attempt to read past the end of file, your handler is passed an empty data object and an error code of 0. For other types of unrecoverable errors, an appropriate error code is returned along with whatever data was read before the error occurred.

## Parameters

- `fd`: The file descriptor from which to read the data.
- `length`: The maximum amount of data to read from the file descriptor.
- `queue`: The queue on which to perform the specified handler block.
- `handler`: The block to schedule for execution when the specified amount of data has been read or an error occurred. The parameters of the handler are as follows:

  - **data**: The data that was read from the file descriptor. This object contains as much data as was currently available from the file descriptor, up to the specified length. This object is owned by the system and released when the handler returns. If you wish to continue using the data, your handler must retain this object or copy the data to another location prior to returning.
  - **error**: This value is `0` if the data was read successfully or an EOF was reached. If an error occurred, this parameter contains the error number.

## See Also

### Reading from the File
- [dispatch_io_read](./dispatch_io_read.md)
  Schedules an asynchronous read operation on the specified channel.
- [dispatch_io_handler_t](./dispatch_io_handler_t.md)
  A handler block used to process operations on a dispatch I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_read)*