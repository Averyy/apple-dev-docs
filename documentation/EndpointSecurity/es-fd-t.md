# es_fd_t

**Framework**: Endpoint Security  
**Kind**: struct

A structure that describes an open file descriptor.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_fd_t
```

## Topics

### Inspecting File Descriptor Properties
- [var fd: Int32](es_fd_t/fd.md)
  The file descriptor number.
- [var fdtype: UInt32](es_fd_t/fdtype.md)
  The file descriptor type, as a libproc type.
### Initializers
- [init()](es_fd_t/init.md)
### Instance Properties
- [var pipe: es_fd_t.__Unnamed_union___Anonymous_field2.__Unnamed_struct_pipe](es_fd_t/pipe-1gtm4.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func es_exec_arg(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](es_exec_arg(_:_:).md)
  Gets the argument at the specified position from a process execution event.
- [func es_exec_arg_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_arg_count(_:).md)
  Gets the number of arguments from a process execution event.
- [func es_exec_env(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](es_exec_env(_:_:).md)
  Gets the environment variable at the specified position from a process execution event.
- [func es_exec_env_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_env_count(_:).md)
  Gets the number of environment variables from a process execution event.
- [func es_exec_fd(UnsafePointer<es_event_exec_t>, UInt32) -> UnsafePointer<es_fd_t>](es_exec_fd(_:_:).md)
  Gets the file descriptor at the specified position from a process execution event.
- [func es_exec_fd_count(UnsafePointer<es_event_exec_t>) -> UInt32](es_exec_fd_count(_:).md)
  Gets the number of file descriptors from a process execution event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_fd_t)*