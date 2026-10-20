# reserved

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An unused field reserved for future use.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[64];
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The source file for the link.
- [var target_dir: UnsafeMutablePointer<es_file_t>](./target_dir.md)
  The directory that contains the newly-created link.
- [var target_filename: es_string_token_t](./target_filename.md)
  The file name of the symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_link_t/reserved)*