# mode

**Framework**: Endpoint Security  
**Kind**: property

The mode argument of the system call.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var mode: mode_t
```

## See Also

- [var source: UnsafeMutablePointer<es_file_t>](es_event_copyfile_t/source.md)
  The file to clone.
- [var target_file: UnsafeMutablePointer<es_file_t>?](es_event_copyfile_t/target_file.md)
  The file, if any, that exists at the target location.
- [var target_dir: UnsafeMutablePointer<es_file_t>](es_event_copyfile_t/target_dir.md)
  The directory that contains the copied file.
- [var target_name: es_string_token_t](es_event_copyfile_t/target_name.md)
  The name of the newly copied file.
- [var flags: Int32](es_event_copyfile_t/flags.md)
  The flags argument of the system call.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_copyfile_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_copyfile_t/mode)*