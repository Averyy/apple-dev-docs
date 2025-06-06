# es_event_link_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the creation of a hard link.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_link_t
```

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](es_event_link_t/source.md)
  The source file for the link.
- [var target_dir: UnsafeMutablePointer<es_file_t>](es_event_link_t/target_dir.md)
  The directory that contains the newly-created link.
- [var target_filename: es_string_token_t](es_event_link_t/target_filename.md)
  The file name of the symbolic link.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_link_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(source: UnsafeMutablePointer<es_file_t>, target_dir: UnsafeMutablePointer<es_file_t>, target_filename: es_string_token_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_link_t/init(source:target_dir:target_filename:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_readlink_t](es_event_readlink_t.md)
  A type for an event that indicates the reading of a symbolic link.
- [struct es_event_unlink_t](es_event_unlink_t.md)
  A type for an event that indicates the deletion of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_link_t)*