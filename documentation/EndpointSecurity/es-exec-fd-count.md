# es_exec_fd_count(_:)

**Framework**: Endpoint Security  
**Kind**: func

Gets the number of file descriptors from a process execution event.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func es_exec_fd_count(_ event: UnsafePointer<es_event_exec_t>) -> UInt32
```

#### Return Value

The number of file descriptors.

## Parameters

- `event`: The process execution event.

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
- [struct es_fd_t](es_fd_t.md)
  A structure that describes an open file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_exec_fd_count(_:))*