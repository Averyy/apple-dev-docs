# filename

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The name of the socket file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var filename: es_string_token_t
```

```c
es_string_token_t filename;
```

## See Also

### Inspecting Event Properties
- [var dir: UnsafeMutablePointer<es_file_t>](./dir.md)
  The directory containing the socket file.
- [var mode: mode_t](./mode.md)
  The mode of the socket file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_bind_t/filename)*