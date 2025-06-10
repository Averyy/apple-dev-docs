# es_exec_arg(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Gets the argument at the specified position from a process execution event.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_exec_arg(_ event: UnsafePointer<es_event_exec_t>, _ index: UInt32) -> es_string_token_t
```

#### Return Value

A string token that contains the argument data and its length.

#### Discussion

This function doesn’t allocate memory for the returned token; it points to a string token inside of `event`. Because you don’t own this memory, don’t try to free it.

> ⚠️ **Warning**:  The returned pointer must not outlive the `event` parameter passed to the function, because the pointer will likely be invalid after the function returns.

## Parameters

- `event`: The process execution event.
- `index`: The zero-based index of the argument to return. Attempting to read an out-of-bounds index — where   — results in undefined behavior.

## See Also

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
- [struct es_fd_t](es_fd_t.md)
  A structure that describes an open file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_exec_arg(_:_:))*