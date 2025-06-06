# es_event_unlink_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the deletion of a file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_unlink_t
```

## Topics

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_file_t>](es_event_unlink_t/target.md)
  The file to unlink.
- [var parent_dir: UnsafeMutablePointer<es_file_t>](es_event_unlink_t/parent_dir.md)
  The directory that contains the file to unlink.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_unlink_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(target: UnsafeMutablePointer<es_file_t>, parent_dir: UnsafeMutablePointer<es_file_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_unlink_t/init(target:parent_dir:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_link_t](es_event_link_t.md)
  A type for an event that indicates the creation of a hard link.
- [struct es_event_readlink_t](es_event_readlink_t.md)
  A type for an event that indicates the reading of a symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_unlink_t)*