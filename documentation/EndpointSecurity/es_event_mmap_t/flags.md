# flags

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Flags that affect the behavior of the memory mapping operation.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var flags: Int32
```

```c
int32_t flags;
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The file to map memory into.
- [var file_pos: UInt64](./file_pos.md)
  The offset into the memory-map file.
- [var max_protection: Int32](./max_protection.md)
  The maximum value you can use for protection flags.
- [var protection: Int32](./protection.md)
  Options that affect the protection of mapped memory pages.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mmap_t/flags)*