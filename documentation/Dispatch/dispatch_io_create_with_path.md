# dispatch_io_create_with_path

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a dispatch I/O channel with the associated path name.

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
extern dispatch_io_tdispatch_io_create_with_path(dispatch_io_type_t type, const char *path, int oflag, mode_t mode, dispatch_queue_t queue, void (^cleanup_handler)(int error));
```

## Return Value

The dispatch I/O channel or `NULL` if an error occurred. The returned object is retained before it is returned; it is your responsibility to close the channel and then release this object when you are done using it.

## Discussion

This function associates the specified path with the channel but does not open a file descriptor for that path until you perform the first I/O operation. While it is open, the channel owns the file descriptor. The channel closes the file descriptor and calls its cleanup handler when one of the following occurs:

- You close the channel by calling the [`dispatch_io_close`](./dispatch_io_close.md) function.
- An unrecoverable error occurs on the file descriptor.
- All references to the channel are released.

## Parameters

- `type`: The type of channel to create. For a list of possible options, see [`dispatch_io_type_t`](./dispatch_io_type_t.md).
- `path`: The file system path to open and use for the channel I/O. This path is opened using the open system call.
- `oflag`: The flags to pass to the open function when opening the path.
- `mode`: The mode to pass to the open function when creating a file at the specified path. If you are not creating a file, specify `0`.
- `queue`: The dispatch queue to associate with the channel. This queue is used to execute the channel’s clean up handler. The channel retains this queue.
- `cleanup_handler`: The block to enqueue when the system relinquishes control of the channel’s file descriptor. This channel takes a single parameter that indicates the reason why control was relinquished. If the `error` parameter contains a non zero value, control was relinquished because there was an error creating the channel; otherwise, this value should be `0`.

## See Also

### Creating a Dispatch I/O Object
- [dispatch_io_create](./dispatch_io_create.md)
  Creates a dispatch I/O channel and associates it with the specified file descriptor.
- [dispatch_io_create_with_io](./dispatch_io_create_with_io.md)
  Creates a new dispatch I/O channel from an existing channel.
- [typealias dispatch_io_t](./dispatch_io_t.md)
  A dispatch I/O channel.
- [dispatch_fd_t](./dispatch_fd_t.md)
  A file descriptor used for I/O operations.
- [OS_dispatch_io](./os_dispatch_io.md)
- [dispatch_io_type_t](./dispatch_io_type_t.md)
  The type of a dispatch I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_create_with_path)*