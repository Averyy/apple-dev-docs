# dispatch_io_read

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Schedules an asynchronous read operation on the specified channel.

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
extern void dispatch_io_read(dispatch_io_t channel, off_t offset, size_t length, dispatch_queue_t queue, dispatch_io_handler_t io_handler);
```

## Discussion

This function reads the specified data and submits the handler block to queue to process the data. If the `done` parameter of the handler is set to false, it means that only part of the data was read. If the `done` parameter is [`true`](../Swift/true.md), it means the read operation is complete and the handler will not be submitted again. If an unrecoverable error occurs on the channel’s file descriptor, the `done` parameter is set to true and an appropriate error value is reported in the handler’s error parameter.

If the handler is submitted with the done parameter set to true, an empty data object, and an error code of 0, it means that the channel reached the end of the file.

## Parameters

- `channel`: The channel to use when reading the data.
- `offset`: For random-access channels, this parameter specifies the offset into the channel from which to read. The offset is specified relative to the initial file pointer of the channel’s file descriptor at the time the channel was created.

  For stream-based channels, this parameter is ignored and data is read from the current position.
- `length`: The number of bytes to read from the channel. Specify `SIZE_MAX` to continue reading data until an EOF is reached.
- `queue`: The dispatch queue on which to submit the `io_handler` block.
- `io_handler`: The block to use to process the data read from the channel. This block may be queued multiple times to process a given data request. Each time the block is queued, the `data` parameter passed to the handler contains the most recently read chunk of data. The handler has no return value and takes the following parameters:

  - **done**: A Boolean value indicating whether the operation is complete.
  - **data**: A [`dispatch_data_t`](./dispatch_data_t.md) object containing the data read from the file descriptor.
  - **error**: An `errno` condition if there was an error; otherwise, the value is `0`.

  Your block need not be reentrant. The system guarantees that only one instance of this block will be executed at any given time.

## See Also

### Reading from the File
- [dispatch_read](./dispatch_read.md)
  Schedules an asynchronous read operation using the specified file descriptor.
- [dispatch_io_handler_t](./dispatch_io_handler_t.md)
  A handler block used to process operations on a dispatch I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_read)*