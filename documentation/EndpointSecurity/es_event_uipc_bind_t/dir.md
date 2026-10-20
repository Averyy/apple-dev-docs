# dir

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The directory containing the socket file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var dir: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * dir;
```

## See Also

### Inspecting Event Properties
- [var filename: es_string_token_t](./filename.md)
  The name of the socket file.
- [var mode: mode_t](./mode.md)
  The mode of the socket file.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_uipc_bind_t/dir)*