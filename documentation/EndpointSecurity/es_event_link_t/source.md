# source

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The source file for the link.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var source: UnsafeMutablePointer<es_file_t>
```

```c
es_file_t * source;
```

## See Also

### Inspecting Event Properties
- [var target_dir: UnsafeMutablePointer<es_file_t>](./target_dir.md)
  The directory that contains the newly-created link.
- [var target_filename: es_string_token_t](./target_filename.md)
  The file name of the symbolic link.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_link_t/source)*