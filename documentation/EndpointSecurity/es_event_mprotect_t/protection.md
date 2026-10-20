# protection

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The protection to apply to the memory-mapped range.

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
- [var address: user_addr_t](./address.md)
  The starting memory address to protect.
- [var size: user_size_t](./size.md)
  The length of the address range to protect.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_mprotect_t/protection)*