# es_event_mprotect_t

**Framework**: Endpoint Security  
**Kind**: struct

A type for an event that indicates a change to protection of memory-mapped pages.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_mprotect_t
```

## Topics

### Inspecting Event Properties
- [var address: user_addr_t](es_event_mprotect_t/address.md)
  The starting memory address to protect.
- [var size: user_size_t](es_event_mprotect_t/size.md)
  The length of the address range to protect.
- [var protection: Int32](es_event_mprotect_t/protection.md)
  The protection to apply to the memory-mapped range.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_mprotect_t/reserved.md)
  An unused field reserved for future use.
### Initializers
- [init()](es_event_mprotect_t/init.md)
- [init(protection: Int32, address: user_addr_t, size: user_size_t, reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](es_event_mprotect_t/init(protection:address:size:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct es_event_mmap_t](es_event_mmap_t.md)
  A type for an event that indicates the mapping of memory to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mprotect_t)*