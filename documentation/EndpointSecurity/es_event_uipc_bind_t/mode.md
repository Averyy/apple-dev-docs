# mode

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The mode of the socket file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var mode: mode_t
```

```c
mode_t mode;
```

## See Also

### Inspecting Event Properties
- [var dir: UnsafeMutablePointer<es_file_t>](./dir.md)
  The directory containing the socket file.
- [var filename: es_string_token_t](./filename.md)
  The name of the socket file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_bind_t/mode)*