# es_event_uipc_bind_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the binding of a socket to a path.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_uipc_bind_t
```

## Topics

### Inspecting Event Properties
- [var dir: UnsafeMutablePointer<es_file_t>](es_event_uipc_bind_t/dir.md)
  The directory containing the socket file.
- [var filename: es_string_token_t](es_event_uipc_bind_t/filename.md)
  The name of the socket file.
- [var mode: mode_t](es_event_uipc_bind_t/mode.md)
  The mode of the socket file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_uipc_bind_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(dir: UnsafeMutablePointer<es_file_t>, filename: es_string_token_t, mode: mode_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_uipc_bind_t/init(dir:filename:mode:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_uipc_connect_t](es_event_uipc_connect_t.md)
  A type for an event that indicates the connection of a socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_bind_t)*