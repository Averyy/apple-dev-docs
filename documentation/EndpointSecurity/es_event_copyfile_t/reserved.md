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
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[56];
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The file to clone.
- [var target_file: UnsafeMutablePointer<es_file_t>?](./target_file.md)
  The file, if any, that exists at the target location.
- [var target_dir: UnsafeMutablePointer<es_file_t>](./target_dir.md)
  The directory that contains the copied file.
- [var target_name: es_string_token_t](./target_name.md)
  The name of the newly copied file.
- [var mode: mode_t](./mode.md)
  The mode argument of the system call.
- [var flags: Int32](./flags.md)
  The flags argument of the system call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_copyfile_t/reserved)*