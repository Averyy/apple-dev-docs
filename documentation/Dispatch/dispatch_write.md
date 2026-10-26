# dispatch_write

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules an asynchronous write operation using the specified file descriptor.

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
extern void dispatch_write(dispatch_fd_t fd, dispatch_data_t data, dispatch_queue_t queue, void (^handler)(dispatch_data_t data, int error));
```

#### Discussion

This is a convenience function for initiating a single, asynchronous write operation at the current position of the specified file descriptor. This method is intended for simple operations where you do not need the overhead of creating a channel and do not plan on issuing more than a few calls to read or write data. Once submitted, there is no way to cancel the write operation.

After calling this function, the system takes control of the specified file descriptor until the handler block is enqueued. While it controls the file descriptor, the system may modify it on behalf of the application. For example, the system typically adds the `O_NONBLOCK` flag to ensure that any operations are non-blocking. During that time, it is an error for your application to modify the file descriptor directly. However, you may pass the file descriptor to this function or the [`dispatch_read`](./dispatch_read.md) function. You may also use the file descriptor to create a new dispatch I/O channel. The system relinquishes control of the file descriptor before calling your handler, so it is safe to modify the file descriptor again from your handler code.

The `handler` you provide is not queued for execution until the write operation finishes. In addition, if you issue multiple read or write calls for the same file descriptor using the convenience APIs, all of those operations must complete before any of the associated handlers are queued. If you are already using the file descriptor with another channel, you should use the [`write(offset:data:queue:ioHandler:)`](./dispatchio/write%28offset,data,queue,iohandler%29.md) function to write data to the channel rather than use this function.

## Parameters

- `fd`: The file descriptor to use when writing the data.
- `data`: The data to write to the file descriptor.
- `queue`: The queue on which to execute the specified handler block.
- `handler`: The block to schedule for execution once the specified data has been written to the file descriptor. The parameters of the handler are as follows:

  - `data` - The data that could not be written to the file descriptor. If the data was written successfully, this parameter is `NULL`.
  - `error` - This value is `0` if the data was written successfully. If an error occurred, this parameter contains the error number.

## See Also

### Writing to the File
- [dispatch_io_write](./dispatch_io_write.md)
  Schedules an asynchronous write operation for the specified channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_write)*