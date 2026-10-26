# dispatch_io_create

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a dispatch I/O channel and associates it with the specified file descriptor.

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
extern dispatch_io_tdispatch_io_create(dispatch_io_type_t type, dispatch_fd_t fd, dispatch_queue_t queue, void (^cleanup_handler)(int error));
```

#### Return Value

The dispatch I/O channel or `NULL` if an error occurred. The returned object is retained before it is returned; it is your responsibility to close the channel and then release this object when you are done using it.

#### Discussion

You use this function to create a dispatch I/O channel for an already open file descriptor. After calling this function, the system takes control of the specified file descriptor until one of the following occurs:

- You close the channel by calling the [`dispatch_io_close`](./dispatch_io_close.md) function.
- An unrecoverable error occurs on the file descriptor.
- All references to the channel are released.

While it controls the file descriptor, the system may modify that file descriptor on behalf of the application. For example, the system typically adds the `O_NONBLOCK` flag to ensure that any operations on the file descriptor are non-blocking. During that time, it is an error for your application to modify the file descriptor directly. However, you may create additional channels using the same file descriptor.

## Parameters

- `type`: The type of channel to create. For a list of possible options, see [`dispatch_io_type_t`](./dispatch_io_type_t.md).
- `fd`: The file descriptor to associate with the channel.
- `queue`: The dispatch queue to associate with the channel. This queue is used to execute the channel’s clean up handler. The channel retains this queue.
- `cleanup_handler`: The block to enqueue when the system relinquishes control of the channel’s file descriptor. This channel takes a single parameter that indicates the reason why control was relinquished. If the `error` parameter contains a non zero value, control was relinquished because there was an error creating the channel; otherwise, this value should be `0`.

## See Also

### Creating a Dispatch I/O Object
- [dispatch_io_create_with_io](./dispatch_io_create_with_io.md)
  Creates a new dispatch I/O channel from an existing channel.
- [dispatch_io_create_with_path](./dispatch_io_create_with_path.md)
  Creates a dispatch I/O channel with the associated path name.
- [typealias dispatch_io_t](./dispatch_io_t.md)
  A dispatch I/O channel.
- [dispatch_fd_t](./dispatch_fd_t.md)
  A file descriptor used for I/O operations.
- [OS_dispatch_io](./os_dispatch_io.md)
- [dispatch_io_type_t](./dispatch_io_type_t.md)
  The type of a dispatch I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_create)*