# dispatch_fd_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

A file descriptor used for I/O operations.

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
typedef int dispatch_fd_t;
```

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
- [OS_dispatch_io](./os_dispatch_io.md)
- [dispatch_io_type_t](./dispatch_io_type_t.md)
  The type of a dispatch I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_fd_t)*