# es_event_uipc_connect_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the connection of a socket.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_uipc_connect_t
```

## Topics

### Inspecting Event Properties
- [var file: UnsafeMutablePointer<es_file_t>](es_event_uipc_connect_t/file.md)
  The socket file bound to the socket.
- [var domain: Int32](es_event_uipc_connect_t/domain.md)
  The communications domain of the socket.
- [var type: Int32](es_event_uipc_connect_t/type.md)
  The type of the socket.
- [var `protocol`: Int32](es_event_uipc_connect_t/protocol.md)
  The protocol of the socket.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_uipc_connect_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(file: UnsafeMutablePointer<es_file_t>, domain: Int32, type: Int32, protocol: Int32, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_uipc_connect_t/init(file:domain:type:protocol:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_uipc_bind_t](es_event_uipc_bind_t.md)
  A type for an event that indicates the binding of a socket to a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_connect_t)*