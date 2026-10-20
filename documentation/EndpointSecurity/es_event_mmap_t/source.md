# source

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The file to map memory into.

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
- [var file_pos: UInt64](./file_pos.md)
  The offset into the memory-map file.
- [var flags: Int32](./flags.md)
  Flags that affect the behavior of the memory mapping operation.
- [var max_protection: Int32](./max_protection.md)
  The maximum value you can use for protection flags.
- [var protection: Int32](./protection.md)
  Options that affect the protection of mapped memory pages.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mmap_t/source)*