# es_exec_arg_count(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Gets the number of arguments from a process execution event.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_exec_arg_count(_ event: UnsafePointer<es_event_exec_t>) -> UInt32
```

```c
extern uint32_t es_exec_arg_count(const es_event_exec_t *event);
```

## Return Value

The number of arguments.

## Parameters

- `event`: The process execution event.

## See Also

### Process Event Helper Functions
- [func es_exec_arg(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](./es_exec_arg%28_,_%29.md)
  Gets the argument at the specified position from a process execution event.
- [func es_exec_env(UnsafePointer<es_event_exec_t>, UInt32) -> es_string_token_t](./es_exec_env%28_,_%29.md)
  Gets the environment variable at the specified position from a process execution event.
- [func es_exec_env_count(UnsafePointer<es_event_exec_t>) -> UInt32](./es_exec_env_count%28_%29.md)
  Gets the number of environment variables from a process execution event.
- [func es_exec_fd(UnsafePointer<es_event_exec_t>, UInt32) -> UnsafePointer<es_fd_t>](./es_exec_fd%28_,_%29.md)
  Gets the file descriptor at the specified position from a process execution event.
- [func es_exec_fd_count(UnsafePointer<es_event_exec_t>) -> UInt32](./es_exec_fd_count%28_%29.md)
  Gets the number of file descriptors from a process execution event.
- [struct es_fd_t](./es_fd_t.md)
  A structure that describes an open file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_exec_arg_count(_:))*