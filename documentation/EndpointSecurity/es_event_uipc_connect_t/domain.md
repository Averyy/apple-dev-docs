# domain

**Framework**: Endpoint Security  
**Kind**: property

The communications domain of the socket.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var domain: Int32
```

#### Discussion

See the man page for `socket(2)` for a list of available domain values.

## See Also

- [var file: UnsafeMutablePointer<es_file_t>](es_event_uipc_connect_t/file.md)
  The socket file bound to the socket.
- [var type: Int32](es_event_uipc_connect_t/type.md)
  The type of the socket.
- [var `protocol`: Int32](es_event_uipc_connect_t/protocol.md)
  The protocol of the socket.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_uipc_connect_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_connect_t/domain)*