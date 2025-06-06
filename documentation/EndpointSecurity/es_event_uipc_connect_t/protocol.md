# protocol

**Framework**: Endpoint Security  
**Kind**: property

The protocol of the socket.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var `protocol`: Int32
```

#### Discussion

See the man page for `socket(2)` for a discussion of the `protocol` parameter.

## See Also

- [var file: UnsafeMutablePointer<es_file_t>](es_event_uipc_connect_t/file.md)
  The socket file bound to the socket.
- [var domain: Int32](es_event_uipc_connect_t/domain.md)
  The communications domain of the socket.
- [var type: Int32](es_event_uipc_connect_t/type.md)
  The type of the socket.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_uipc_connect_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_connect_t/protocol)*