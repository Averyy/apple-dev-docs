# es_event_mmap_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates the mapping of memory to a file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_mmap_t
```

## Topics

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](es_event_mmap_t/source.md)
  The file to map memory into.
- [var file_pos: UInt64](es_event_mmap_t/file_pos.md)
  The offset into the memory-map file.
- [var flags: Int32](es_event_mmap_t/flags.md)
  Flags that affect the behavior of the memory mapping operation.
- [var max_protection: Int32](es_event_mmap_t/max_protection.md)
  The maximum value you can use for protection flags.
- [var protection: Int32](es_event_mmap_t/protection.md)
  Options that affect the protection of mapped memory pages.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_mmap_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init(protection: Int32, max_protection: Int32, flags: Int32, file_pos: UInt64, source: UnsafeMutablePointer<es_file_t>, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_mmap_t/init(protection:max_protection:flags:file_pos:source:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct es_event_mprotect_t](es_event_mprotect_t.md)
  A type for an event that indicates a change to protection of memory-mapped pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mmap_t)*