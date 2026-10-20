# protection

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

Options that affect the protection of mapped memory pages.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var protection: Int32
```

```c
int32_t protection;
```

## See Also

### Inspecting Event Properties
- [var source: UnsafeMutablePointer<es_file_t>](./source.md)
  The file to map memory into.
- [var file_pos: UInt64](./file_pos.md)
  The offset into the memory-map file.
- [var flags: Int32](./flags.md)
  Flags that affect the behavior of the memory mapping operation.
- [var max_protection: Int32](./max_protection.md)
  The maximum value you can use for protection flags.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mmap_t/protection)*