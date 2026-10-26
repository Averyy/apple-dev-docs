# dispatch_io_type_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

The type of a dispatch I/O channel.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef unsigned long dispatch_io_type_t;
```

## Topics

### I/O Access Type
- [var DISPATCH_IO_STREAM: Int32](./dispatch_io_stream.md)
- [var DISPATCH_IO_RANDOM: Int32](./dispatch_io_random.md)

## See Also

### Creating a Dispatch I/O Object
- [dispatch_io_create](./dispatch_io_create.md)
  Creates a dispatch I/O channel and associates it with the specified file descriptor.
- [dispatch_io_create_with_io](./dispatch_io_create_with_io.md)
  Creates a new dispatch I/O channel from an existing channel.
- [dispatch_io_create_with_path](./dispatch_io_create_with_path.md)
  Creates a dispatch I/O channel with the associated path name.
- [typealias dispatch_io_t](./dispatch_io_t.md)
  A dispatch I/O channel.
- [dispatch_fd_t](./dispatch_fd_t.md)
  A file descriptor used for I/O operations.
- [OS_dispatch_io](./os_dispatch_io.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_type_t)*