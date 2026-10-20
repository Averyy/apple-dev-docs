# file

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The socket file bound to the socket.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var file: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * file;
```

## See Also

### Inspecting Event Properties
- [var domain: Int32](./domain.md)
  The communications domain of the socket.
- [var type: Int32](./type.md)
  The type of the socket.
- [var `protocol`: Int32](./protocol.md)
  The protocol of the socket.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_connect_t/file)*