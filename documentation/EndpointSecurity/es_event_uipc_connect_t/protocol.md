# protocol

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The protocol of the socket.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var `protocol`: Int32
```

```c
int protocol;
```

#### Discussion

See the man page for `socket(2)` for a discussion of the `protocol` parameter.

## See Also

### Inspecting Event Properties
- [var file: UnsafeMutablePointer<es_file_t>](./file.md)
  The socket file bound to the socket.
- [var domain: Int32](./domain.md)
  The communications domain of the socket.
- [var type: Int32](./type.md)
  The type of the socket.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_connect_t/protocol)*