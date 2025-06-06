# file_pos

**Framework**: Endpoint Security  
**Kind**: property

The offset into the memory-map file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var file_pos: UInt64
```

## See Also

- [var source: UnsafeMutablePointer<es_file_t>](es_event_mmap_t/source.md)
  The file to map memory into.
- [var flags: Int32](es_event_mmap_t/flags.md)
  Flags that affect the behavior of the memory mapping operation.
- [var max_protection: Int32](es_event_mmap_t/max_protection.md)
  The maximum value you can use for protection flags.
- [var protection: Int32](es_event_mmap_t/protection.md)
  Options that affect the protection of mapped memory pages.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_mmap_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mmap_t/file_pos)*